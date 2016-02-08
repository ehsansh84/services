__author__ = 'Ehsan'
import sys
sys.path.append("/root/ehsan/services")
from public_data import *
import feedparser
# import rss_data
from rss_data import rss_links

col_news = db['news']


def exists(link):
    results = col_news.find({'link': link})
    if results.count() <> 0:
        for item in results:
            # print('ITEM:', item)
            # print('RESULT OF EXISTS:', item['sub_category'][0])
            return item['sub_category'][0]
    else:
        return 0


def fetch(rss_item):
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
            # 'date': item['date'],
            # 'date_parsed': item['date_parsed'],
        }
        t_item = exists(news_item['link'])

        if t_item == 0:
            # print('t_ITEM is 0')
            col_news.insert(news_item)
            new_count += 1
        else:
            if t_item in news_item['sub_category']:
                dup_count += 1
                # print('DUP news')
            else:
                print('===========================================================')
                print('SUB_CAT:', news_item['sub_category']),
                print('ITEM:', t_item)
                news_item['sub_category'].append(t_item)
                col_news.update_one({'link': news_item['link']}, {
                    "$set": {'sub_category': news_item['sub_category']}
                })
                # exit()
    print('There are %s duplicates and %s new from %s' % (dup_count, new_count, rss_item['category']))

total_count_old = col_news.count()
for item in rss_links:
    fetch(item)
total_count_new = col_news.count()

print('Total news was %s and now it''s %s, added %s:' % (total_count_old, total_count_new, total_count_new - total_count_old)),
