__author__ = 'Ehsan'
import sys
sys.path.append("/root/ehsan/services")
from public_data import *
import feedparser
from tools import *
# import rss_data
# from rss_data import rss_links
from datetime import  datetime

# print(str(sys.argv))
# try:
#     s = sys.argv[1]
# except:
#     pass
# print(s)
# exit()


col_news = db['news']
col_rss = db['rss']
col_rss_log = db['rss_log']
t = timer()


def exists(link):
    return col_news.find({'link': link}).limit(1).count()


def fetch(rss_item):
    try:
        t.start()
        dup_count = 0
        new_count = 0
        # log.color_print(color=Color.CYAN, text=rss_item['link'])
        feed = feedparser.parse(rss_item['link'])
        for item in feed["items"]:
            # t.start()
            news_item = {
                'source': rss_item['source'],
                'category': rss_item['category'],
                'sub_category': rss_item['sub_category'],
                'title': item['title'],
                'su mmary': item['summary'],
                'link': item['link'],
                'text': ''
                # 'date': item['date'],
                # 'date_parsed': item['date_parsed'],
            }
            # t1 = timer()
            # t1.start()
            t_item = exists(news_item['link'])
            # exist_time = t1.end()

            if t_item == 0:
                # print('t_ITEM is 0')
                # t.start()
                # col_news.insert(news_item)
                # print('Took %s seconds for insert!' % t.end())
                new_count += 1
            else:
                # if t_item in news_item['sub_category']:
                dup_count += 1
                    # print('DUP news')
                # else:
                #     print('===========================================================')
                #     print('SUB_CAT:', news_item['sub_category']),
                #     print('ITEM:', t_item)
                #     news_item['sub_category'].append(t_item)
                #     col_news.update_one({'link': news_item['link']}, {
                #         "$set": {'sub_category': news_item['sub_category']}
                #     })
                    # exit()
            # print('Total %s seconds - Check Exists %s' % (t.end(), exist_time))
        duration = t.end()
        link = rss_item['link']
        print('DUP: %s NEW: %s TIME: %s SOURCE: %s LINK: %s' % (dup_count, new_count, duration, rss_item['category'], link))
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
if exec_type == 'micro':
    rss_links = col_rss.find({'duration': {'$lt': 6}})
elif exec_type == 'small':
    rss_links = col_rss.find({'duration': {'$lt': 10}})
elif exec_type == 'large':
    rss_links = col_rss.find({'duration': {'$gte': 10}})
else:
    rss_links = col_rss.find({})


try:
    for item in rss_links:
        # t.start()
        # if i < 90:
        #     print(i)
        #     i += 1
        #     continue
        try:
            if item['active'] == 1:
                print(i),
                # print(str(item))
                fetch(item)
        except Exception, e:
            log.color_print(text=log.get_exception(), color=Color.BLUE)
            print('ERROR: %s' % e.message)
            print('%s - Source: %s, Category: %s, Sub Category: %s' % (i, item['source'], item['category'], item['sub_category']))
            error_count += 1
        i += 1
        # print('Took %s seconds for this item' % t.end())

    total_count_new = col_news.count()
    print('Total news was %s and now it''s %s, added %s:' % (total_count_old, total_count_new, total_count_new - total_count_old)),
    print('Oops! %s Errors happend!' % error_count)
except Exception, e:
    log.color_print(text=log.get_exception(), color=Color.RED)
    print('Error:= => %s' % e.message)
    print('Error:= => %s' % str(e.args))
