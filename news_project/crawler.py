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
    {'source': 'nytimes', 'category': 'Health', 'sub_category': ['Health'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Health.xml'},
    {'source': 'nytimes', 'category': 'Health', 'sub_category': ['Research'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Research.xml'},
    {'source': 'nytimes', 'category': 'Health', 'sub_category': ['Money & Policy'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/HealthCarePolicy.xml'},
    {'source': 'nytimes', 'category': 'Health', 'sub_category': ['Fitness & Nutrition'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Nutrition.xml'},
    {'source': 'nytimes', 'category': 'Health', 'sub_category': ['Views'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Views.xml'},
    {'source': 'nytimes', 'category': 'Arts', 'sub_category': ['Arts'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Arts.xml'},
    {'source': 'nytimes', 'category': 'Arts', 'sub_category': ['Dance'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Dance.xml'},
    {'source': 'nytimes', 'category': 'Arts', 'sub_category': ['Theater'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Theater.xml'},
    {'source': 'nytimes', 'category': 'Arts', 'sub_category': ['International Arts'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/InternationalArts.xml'},
    {'source': 'nytimes', 'category': 'Arts', 'sub_category': ['Movies'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Movies.xml'},
    {'source': 'nytimes', 'category': 'Arts', 'sub_category': ['Artsbeat Blog'], 'link': 'http://artsbeat.blogs.nytimes.com/feed'},
    {'source': 'nytimes', 'category': 'Arts', 'sub_category': ['Art & Design'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/ArtandDesign.xml'},
    {'source': 'nytimes', 'category': 'Arts', 'sub_category': ['Music'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Music.xml'},
    {'source': 'nytimes', 'category': 'Arts', 'sub_category': ['Carpetbagger Blog'], 'link': 'http://carpetbagger.blogs.nytimes.com/feed'},
    {'source': 'nytimes', 'category': 'Arts', 'sub_category': ['Books'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Books.xml'},
    {'source': 'nytimes', 'category': 'Arts', 'sub_category': ['Television'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Television.xml'},
    {'source': 'nytimes', 'category': 'Style', 'sub_category': ['Fashion & Style'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/FashionandStyle.xml'},
    {'source': 'nytimes', 'category': 'Style', 'sub_category': ['Dining & Wine'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/DiningandWine.xml'},
    {'source': 'nytimes', 'category': 'Style', 'sub_category': ['Weddings/Celebrations'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Weddings.xml'},
    {'source': 'nytimes', 'category': 'Style', 'sub_category': ['T Magazine'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/tmagazine.xml'},
    {'source': 'nytimes', 'category': 'Style', 'sub_category': ['International Style'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/InternationalStyle.xml'},
    {'source': 'nytimes', 'category': 'Style', 'sub_category': ['Home & Garden'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/HomeandGarden.xml'},
    {'source': 'nytimes', 'category': 'Style', 'sub_category': ['Motherlode Blog'], 'link': 'http://parenting.blogs.nytimes.com/feed/'},
    {'source': 'nytimes', 'category': 'Travel', 'sub_category': ['Travel'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Travel.xml'},
    {'source': 'nytimes', 'category': 'Travel', 'sub_category': ['Frugal Traveler'], 'link': 'http://topics.nytimes.com/top/features/travel/columns/frugal_traveler/index.html?rss=1'},
    {'source': 'nytimes', 'category': 'Magazine', 'sub_category': ['6th Floor Blog'], 'link': 'http://6thfloor.blogs.nytimes.com/feed/'},
    {'source': 'nytimes', 'category': 'Jobs', 'sub_category': ['Jobs'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/JobMarket.xml'},
    {'source': 'nytimes', 'category': 'Real Estate', 'sub_category': ['Real Estate'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/RealEstate.xml'},
    {'source': 'nytimes', 'category': 'Real Estate', 'sub_category': ['Commercial'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Commercial.xml'},
    {'source': 'nytimes', 'category': 'Autos', 'sub_category': ['Autos'], 'link': 'http://www.nytimes.com/services/xml/rss/nyt/Automobiles.xml'},
    {'source': 'bbc', 'category': 'Top Stories', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/rss.xml'},
    {'source': 'bbc', 'category': 'World', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/world/rss.xml'},
    {'source': 'bbc', 'category': 'UK', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/uk/rss.xml'},
    {'source': 'bbc', 'category': 'Business', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/business/rss.xml'},
    {'source': 'bbc', 'category': 'Politics', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/politics/rss.xml'},
    {'source': 'bbc', 'category': 'Health', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/health/rss.xml'},
    {'source': 'bbc', 'category': 'Education & Family', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/education/rss.xml'},
    {'source': 'bbc', 'category': 'Science & Environment', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/science_and_environment/rss.xml'},
    {'source': 'bbc', 'category': 'Technology', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/technology/rss.xml'},
    {'source': 'bbc', 'category': 'Entertainment & Arts', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml'},
    {'source': 'bbc', 'category': 'Africa', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/world/africa/rss.xml'},
    {'source': 'bbc', 'category': 'Asia', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/world/asia/rss.xml'},
    {'source': 'bbc', 'category': 'Europe', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/world/europe/rss.xml'},
    {'source': 'bbc', 'category': 'Latin America', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/world/latin_america/rss.xml'},
    {'source': 'bbc', 'category': 'Middle East', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/world/middle_east/rss.xml'},
    {'source': 'bbc', 'category': 'US & Canada', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml'},
    {'source': 'bbc', 'category': 'England', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/england/rss.xml'},
    {'source': 'bbc', 'category': 'Northern Ireland', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/northern_ireland/rss.xml'},
    {'source': 'bbc', 'category': 'Scotland', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/scotland/rss.xml'},
    {'source': 'bbc', 'category': 'Wales', 'sub_category': [''], 'link': 'http://feeds.bbci.co.uk/news/wales/rss.xml'},
    {'source': 'cnn', 'category': 'Top Stories', 'sub_category': [''], 'link': 'http://rss.cnn.com/rss/cnn_topstories.rss'},
    {'source': 'cnn', 'category': 'World', 'sub_category': [''], 'link': 'http://rss.cnn.com/rss/cnn_world.rss'},
    {'source': 'cnn', 'category': 'U.S.	', 'sub_category': [''], 'link': 'http://rss.cnn.com/rss/cnn_us.rss'},
    {'source': 'cnn', 'category': 'Business', 'sub_category': [''], 'link': 'http://rss.cnn.com/rss/money_latest.rss'},
    {'source': 'cnn', 'category': 'Politics', 'sub_category': [''], 'link': 'http://rss.cnn.com/rss/cnn_allpolitics.rss'},
    {'source': 'cnn', 'category': 'Technology', 'sub_category': [''], 'link': 'http://rss.cnn.com/rss/cnn_tech.rss'},
    {'source': 'cnn', 'category': 'Health', 'sub_category': [''], 'link': 'http://rss.cnn.com/rss/cnn_health.rss'},
    {'source': 'cnn', 'category': 'Entertainment', 'sub_category': [''], 'link': 'http://rss.cnn.com/rss/cnn_showbiz.rss'},
    {'source': 'cnn', 'category': 'Travel', 'sub_category': [''], 'link': 'http://rss.cnn.com/rss/cnn_travel.rss'},
    {'source': 'cnn', 'category': 'Living', 'sub_category': [''], 'link': 'http://rss.cnn.com/rss/cnn_living.rss'},
    {'source': 'cnn', 'category': 'CNN Student News', 'sub_category': [''], 'link': 'http://rss.cnn.com/services/podcasting/studentnews/rss.xml'},
    {'source': 'cnn', 'category': 'Most Recent', 'sub_category': [''], 'link': 'http://rss.cnn.com/rss/cnn_latest.rss'},
    {'source': 'cnn', 'category': 'iReports on CNN', 'sub_category': [''], 'link': 'http://rss.ireport.com/feeds/oncnn.rss'},
    {'source': 'euronews', 'category': 'home', 'sub_category': [''], 'link': 'http://feeds.feedburner.com/euronews/en/home/'},
    {'source': 'euronews', 'category': 'News', 'sub_category': [''], 'link': 'http://feeds.feedburner.com/euronews/en/news/'},
    {'source': 'euronews', 'category': 'Business', 'sub_category': [''], 'link': 'http://feeds.feedburner.com/euronews/en/business/'},
    {'source': 'euronews', 'category': 'no comment', 'sub_category': [''], 'link': 'http://feeds.feedburner.com/euronews/en/Euronews-NoComment/'},
    {'source': 'euronews', 'category': 'European Affairs', 'sub_category': [''], 'link': 'http://feeds.feedburner.com/euronews/en/europa/'},
    {'source': 'euronews', 'category': 'Sci-tech', 'sub_category': [''], 'link': 'http://feeds.feedburner.com/euronews/en/sci-tech/'},
    {'source': 'euronews', 'category': 'Culture', 'sub_category': [''], 'link': 'http://feeds.feedburner.com/euronews/en/lifestyle/'},
    {'source': 'france24', 'category': 'World', 'sub_category': [''], 'link': 'http://www.france24.com/en/top-stories/rss'},
    {'source': 'france24', 'category': 'Europe', 'sub_category': [''], 'link': 'http://www.france24.com/en/europe/rss'},
    {'source': 'france24', 'category': 'France', 'sub_category': [''], 'link': 'http://www.france24.com/en/france/rss'},
    {'source': 'france24', 'category': 'Africa', 'sub_category': [''], 'link': 'http://www.france24.com/en/africa/rss'},
    {'source': 'france24', 'category': 'Middle East', 'sub_category': [''], 'link': 'http://www.france24.com/en/middle-east/rss'},
    {'source': 'france24', 'category': 'Americas', 'sub_category': [''], 'link': 'http://www.france24.com/en/americas/rss'},
    {'source': 'france24', 'category': 'Asia/Pacific', 'sub_category': [''], 'link': 'http://www.france24.com/en/asia-pacific/rss'},
    {'source': 'france24', 'category': 'Business/Tech', 'sub_category': [''], 'link': 'http://www.france24.com/en/business/rss'},
    {'source': 'france24', 'category': 'Sports', 'sub_category': [''], 'link': 'http://www.france24.com/en/sport/rss'},
    {'source': 'france24', 'category': 'Culture', 'sub_category': [''], 'link': 'http://www.france24.com/en/culture/rss'},
    {'source': 'france24', 'category': 'Earth', 'sub_category': [''], 'link': 'http://www.france24.com/en/earth/rss'},
    {'source': 'france24', 'category': 'Health', 'sub_category': [''], 'link': 'http://www.france24.com/en/health/rss'},
    {'source': 'france24', 'category': 'Blogs', 'sub_category': [''], 'link': 'http://blogs.france24.com/blog_feed.rss/fr'},
    {'source': 'abcnews', 'category': 'Top Stories', 'sub_category': [''], 'link': 'http://feeds.abcnews.com/abcnews/topstories'},
    {'source': 'abcnews', 'category': 'World Headlines', 'sub_category': [''], 'link': 'http://feeds.abcnews.com/abcnews/internationalheadlines'},
    {'source': 'abcnews', 'category': 'US Headlines', 'sub_category': [''], 'link': 'http://feeds.abcnews.com/abcnews/usheadlines'},
    {'source': 'abcnews', 'category': 'Politics Headlines', 'sub_category': [''], 'link': 'http://feeds.abcnews.com/abcnews/politicsheadlines'},
    {'source': 'abcnews', 'category': 'The Blotter from Brian Ross', 'sub_category': [''], 'link': 'http://feeds.abcnews.com/abcnews/blotterheadlines'},
    {'source': 'abcnews', 'category': 'Cuomo on the Case', 'sub_category': [''], 'link': 'http://feeds.abcnews.com/abcnews/thelawheadlines'},
    {'source': 'abcnews', 'category': 'Money Headlines', 'sub_category': [''], 'link': 'http://feeds.abcnews.com/abcnews/moneyheadlines'},
    {'source': 'abcnews', 'category': 'Technology Headlines', 'sub_category': [''], 'link': 'http://feeds.abcnews.com/abcnews/technologyheadlines'},
    {'source': 'abcnews', 'category': 'Health Headlines', 'sub_category': [''], 'link': 'http://feeds.abcnews.com/abcnews/healthheadlines'},
    {'source': 'abcnews', 'category': 'Entertainment Headlines', 'sub_category': [''], 'link': 'http://feeds.abcnews.com/abcnews/entertainmentheadlines'},
    {'source': 'abcnews', 'category': 'Travel Headlines', 'sub_category': [''], 'link': 'http://feeds.abcnews.com/abcnews/travelheadlines'},
    {'source': 'abcnews', 'category': 'ESPN Sports', 'sub_category': [''], 'link': 'http://feeds.abcnews.com/abcnews/sportsheadlines'},
    {'source': 'abcnews', 'category': 'World News Headlines', 'sub_category': [''], 'link': 'http://feeds.abcnews.com/abcnews/worldnewsheadlines'},
    {'source': 'abcnews', 'category': '20/20 Headlines', 'sub_category': [''], 'link': 'http://feeds.abcnews.com/abcnews/2020headlines'},
    {'source': 'abcnews', 'category': 'Primetime Headlines', 'sub_category': [''], 'link': 'http://feeds.abcnews.com/abcnews/primetimeheadlines'},
    {'source': 'abcnews', 'category': 'Nightline Headlines', 'sub_category': [''], 'link': 'http://feeds.abcnews.com/abcnews/nightlineheadlines'},
    {'source': 'abcnews', 'category': 'Good Morning America Headlines', 'sub_category': [''], 'link': 'http://feeds.abcnews.com/abcnews/gmaheadlines'},
    {'source': 'abcnews', 'category': 'This Week Headlines', 'sub_category': [''], 'link': 'http://feeds.abcnews.com/abcnews/thisweekheadlines'},
    # {'source': 'abcnews', 'category': 'Style', 'sub_category': [''], 'link': ''},
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
# print(col_news.count())


# print(feed["bozo"])
# print(feed["url"])
# print(feed["version"])
# print(feed["channel"])
# print(feed["items"])

