__author__ = 'Ehsan'
import sys
sys.path.append("/root/ehsan/services")
from public_data import *
import feedparser

# rss_link = 'http://www.nytimes.com/services/xml/rss/nyt/MiddleEast.xml'
rss_links = [
    {'source': 'nytimes', 'category': 'world', 'sub_category': ['world'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/World.xml'},
    {'source': 'nytimes', 'category': 'world', 'sub_category': ['africa'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Africa.xml'},
    {'source': 'nytimes', 'category': 'world', 'sub_category': ['americas'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Americas.xml'},
    {'source': 'nytimes', 'category': 'world', 'sub_category': ['asia pacific'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml'},
    {'source': 'nytimes', 'category': 'world', 'sub_category': ['europe'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Europe.xml'},
    {'source': 'nytimes', 'category': 'world', 'sub_category': ['middle east'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/MiddleEast.xml'},
    {'source': 'nytimes', 'category': 'U.S', 'sub_category': ['U.S'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/US.xml'},
    {'source': 'nytimes', 'category': 'U.S', 'sub_category': ['education'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Education.xml'},
    {'source': 'nytimes', 'category': 'U.S', 'sub_category': ['politics'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Politics.xml'},
    {'source': 'nytimes', 'category': 'N.Y./Region', 'sub_category': ['N.Y./Region'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/NYRegion.xml'},
    {'source': 'nytimes', 'category': 'N.Y./Region', 'sub_category': ['City Room Blog'], 'link': 'http://cityroom.blogs.nytimes.com/feed/'},
    {'source': 'nytimes', 'category': 'N.Y./Region', 'sub_category': ['Fort Greene, NY Blog'], 'link': 'http://fort-greene.blogs.nytimes.com/feed'},
    {'source': 'nytimes', 'category': 'N.Y./Region', 'sub_category': ['East Village Blog'], 'link': 'http://eastvillage.thelocal.nytimes.com/feed/'},
    {'source': 'nytimes', 'category': 'Business', 'sub_category': ['Business'], 'link': 'http://feeds.nytimes.com/nyt/rss/Business'},
    {'source': 'nytimes', 'category': 'Business', 'sub_category': ['Small Business'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/SmallBusiness.xml'},
    {'source': 'nytimes', 'category': 'Business', 'sub_category': ['DealBook'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Dealbook.xml'},
    {'source': 'nytimes', 'category': 'Business', 'sub_category': ['Energy & Environment'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/EnergyEnvironment.xml'},
    {'source': 'nytimes', 'category': 'Business', 'sub_category': ['Media & Advertising'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/MediaandAdvertising.xml'},
    {'source': 'nytimes', 'category': 'Business', 'sub_category': ['International Business'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/InternationalBusiness.xml'},
    {'source': 'nytimes', 'category': 'Business', 'sub_category': ['Economy'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Economy.xml'},
    {'source': 'nytimes', 'category': 'Business', 'sub_category': ['Your Money'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/YourMoney.xml'},
    {'source': 'nytimes', 'category': 'Technology', 'sub_category': ['Technology'], 'link': 'http://feeds.nytimes.com/nyt/rss/Technology'},
    {'source': 'nytimes', 'category': 'Technology', 'sub_category': ['Bits Blog'], 'link': 'http://bits.blogs.nytimes.com/feed/'},
    {'source': 'nytimes', 'category': 'Technology', 'sub_category': ['Personal Tech'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/PersonalTech.xml'},
    {'source': 'nytimes', 'category': 'Sport', 'sub_category': ['Sports'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Sports.xml'},
    {'source': 'nytimes', 'category': 'Sport', 'sub_category': ['College Football'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/CollegeFootball.xml'},
    {'source': 'nytimes', 'category': 'Sport', 'sub_category': ['Pro-Football'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/ProFootball.xml'},
    {'source': 'nytimes', 'category': 'Sport', 'sub_category': ['International Sports'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/InternationalSports.xml'},
    {'source': 'nytimes', 'category': 'Sport', 'sub_category': ['Golf'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Golf.xml'},
    {'source': 'nytimes', 'category': 'Sport', 'sub_category': ['Soccer'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Soccer.xml'},
    {'source': 'nytimes', 'category': 'Sport', 'sub_category': ['Baseball'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Baseball.xml'},
    {'source': 'nytimes', 'category': 'Sport', 'sub_category': ['Hockey'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Hockey.xml'},
    {'source': 'nytimes', 'category': 'Sport', 'sub_category': ['Tennis'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Tennis.xml'},
    {'source': 'nytimes', 'category': 'Sport', 'sub_category': ['College Basketball'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/CollegeBasketball.xml'},
    {'source': 'nytimes', 'category': 'Sport', 'sub_category': ['Pro-Basketball'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/ProBasketball.xml'},
    {'source': 'nytimes', 'category': 'Sport', 'sub_category': ['Gambit Blog'], 'link': 'http://gambit.blogs.nytimes.com/feed/'},
    # {'source': 'nytimes', 'category': 'Sport', 'sub_category': [], 'link': ''},
    # {'source': 'nytimes', 'category': 'Sport', 'sub_category': [], 'link': ''},
]
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
        else:
            if t_item in news_item['sub_category']:
                print('DUP news')
            else:
                print('===========================================================')
                print('SUB_CAT:', news_item['sub_category']),
                print('ITEM:', t_item)
                news_item['sub_category'].append(t_item)
                col_news.update_one({'link': news_item['link']}, {
                    "$set": {'sub_category': news_item['sub_category']}
                })
                # exit()

print('Total news is:'),
print(col_news.count())
for item in rss_links:
    print(item['category'])
    fetch(item)
print('Total news is:'),
print(col_news.count())


# print(feed["bozo"])
# print(feed["url"])
# print(feed["version"])
# print(feed["channel"])
# print(feed["items"])

