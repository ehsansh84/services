__author__ = 'Ehsan'
import sys
sys.path.append("/root/ehsan/services")
from public_data import *
import feedparser
from tools import *
from datetime import datetime, timedelta

col_news = db_bigtc['news']
col_rss = db_bigtc['rss']
col_rss_log = db_bigtc['rss_log']
col_errors_log = db_bigtc['errors_log']
t = timer()
total_time = timer()


def exists(link):
    return col_news.find({'link': link}).limit(1).count()


def fetch(rss_item):
    try:
        t.start()
        dup_count = 0
        new_count = 0
        feed = feedparser.parse(rss_item['link'])
        for item in feed["items"]:
            news_item = {
                'source': rss_item['source'],
                'category': rss_item['category'],
                'sub_category': rss_item['sub_category'],
                'title': item['title'],
                'summary': item['summary'],
                'link': item['link'],
                'text': ''
            }
            t_item = exists(news_item['link'])
            if t_item == 0:
                # log.color_print(text='News Item Added!', color=Color.LIME)
                col_news.insert(news_item)
                new_count += 1
            else:
                dup_count += 1
        duration = t.end()
        link = rss_item['link']
        log.color_print(color=Color.LIME, text='DUP: %s NEW: %s TIME: %s SOURCE: %s LINK: %s' % (dup_count, new_count, duration, rss_item['category'], link))
        total_count = new_count + dup_count
        last_read = datetime.now()
        col_rss.update({'link': link}, {"$set": {
            'total_count': total_count,
            'duplicates': dup_count,
            'new': new_count,
            'last_read': last_read,
            'duration': duration
        }})

        col_rss_log.insert({
            'link': link,
            'total_count': total_count,
            'duplicates': dup_count,
            'new': new_count,
            'last_read': last_read,
            'duration': duration
        })
    except:
        log.color_print(text=log.get_exception(), color=Color.YELLOW)

total_count_old = col_news.count()
error_count = 0
i = 1

exec_type = 'all'
try:
    exec_type = sys.argv[1]
except:
    pass

d = (datetime.now() - timedelta(hours=4))
print(datetime.now())
print(d)
if exec_type == 'new':
    rss_links = col_rss.find({'duration': -1, 'last_read': {'$gt':  d}})
    rss_count = col_rss.count({'duration': -1, 'last_read': {'$gt':  d}})
if exec_type == 'micro':
    rss_links = col_rss.find({'duration': {'$lt': 6}, 'active': 1, 'last_read': {'$gt':  d}}).sort('duration', 1)
    rss_count = col_rss.count({'duration': {'$lt': 6}, 'active': 1, 'last_read': {'$gt':  d}})
elif exec_type == 'small':
    rss_links = col_rss.find({'duration': {'$lt': 10}, 'active': 1, 'last_read': {'$gt':  d}}).sort('duration', 1)
    rss_count = col_rss.count({'duration': {'$lt': 10}, 'active': 1, 'last_read': {'$gt':  d}})
elif exec_type == 'large':
    rss_links = col_rss.find({'duration': {'$gte': 10}, 'active': 1, 'last_read': {'$gt':  d}}).sort('duration', 1)
    rss_count = col_rss.count({'duration': {'$gte': 10}, 'active': 1, 'last_read': {'$gt':  d}})
elif exec_type == 'huge':
    rss_links = col_rss.find({'duration': {'$gte': 30}, 'active': 1, 'last_read': {'$gt':  d}}).sort('duration', 1)
    rss_count = col_rss.count({'duration': {'$gte': 30}, 'active': 1, 'last_read': {'$gt':  d}})
else:
    rss_links = col_rss.find({'active': 1, 'last_read': {'$gt':  d}}).sort('duration', 1)
    rss_count = col_rss.count({'active': 1, 'last_read': {'$gt':  d}})

log.color_print(text='processing %s RSS' % rss_count, color=Color.BLUE)

link_processing = ''
duration = 0
try:
    total_time.start()
    for item in rss_links:
        try:
            t.start()
            link_processing = item['link']
            log.color_print(text='processing %s with link %s' % (item['duration'], item['link']), color=Color.YELLOW)
            if item['active'] == 1:
                print(i),
                fetch(item)
        except Exception, e:
            log.color_print(text=log.get_exception(), color=Color.BLUE)
            # print('ERROR: %s' % e.message)
            # print('%s - Source: %s, Category: %s, Sub Category: %s' % (i, item['source'], item['category'], item['sub_category']))
            error_count += 1
        i += 1
        duration = t.end()
        log.color_print(text='it took %s this time!' % (duration), color=Color.LIME)


    total_count_new = col_news.count()
    log.color_print(color=Color.BLUE,
                    text='Mode: %s, Errors: %s Total news was %s and now it''s %s, added %s total time: %s' % (exec_type, error_count, total_count_old, total_count_new, total_count_new - total_count_old, total_time.end())),
    # print('Oops! %s Errors happend!' % error_count)
except Exception, e:
    time = total_time.end()
    log.color_print(text=log.get_exception(), color=Color.RED)
    log.color_print(text=log.get_exception(), color=Color.RED)
    log.color_print(text='it took %s this time! and error stopped it! total time: %s' % (t.end(), time), color=Color.LIME)
    col_errors_log.insert({'exception_details': log.get_exception(), 'link': link_processing, 'duration': duration, 'total_time': time})
    # print('Error:= => %s' % e.message)
    # print('Error:= => %s' % str(e.args))
