__author__ = 'Ehsan'
import sys
sys.path.append("/root/ehsan/services")
from public_data import *
rss_link = 'http://www.nytimes.com/services/xml/rss/nyt/MiddleEast.xml'
col_news = db['news']

import feedparser

feed = feedparser.parse(rss_link)

# print(feed["bozo"])
# print(feed["url"])
# print(feed["version"])
# print(feed["channel"])
# print(feed["items"])
for item in feed["items"]:
    print(item)
    news_item = {
        'title': item['title'],
        'summary': item['summary'],
        'date': item['date'],
        'date_parsed': item['date_parsed'],
        'link': item['link'],
        'text': ''
    }

    col_news.insert(news_item)
