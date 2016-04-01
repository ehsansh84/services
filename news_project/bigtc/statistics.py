import sys
sys.path.append("/root/ehsan/services")
from public_data import *

col = db['news']
col_statistics = db['statistics']
col_categories = db['categories']
col_sub_categories = db['sub_categories']
col_rss = db['rss']
col_sources = db['sources']


def extract_categories():
    categories = []
    sub_categories = []

    i = 0
    news = col.find({})

    # Extract all news categories and sub categories
    try:
        for item in news:
            if not item['category'] in categories:
                categories.append(item['category'])

            # if len(item['sub_category']) == 1:
            #     if not item['sub_category'] in sub_categories:
            #         sub_categories.append(item['sub_category'])
            # else:
            #     print(item['sub_category'])
            i += 1

            if i % 1000 == 0:
                print(i)
    except Exception, e:
        print('ERROR: '+e.message)

    # Send them to collection
    for item in categories:
        col_categories.insert({'name': item})
    for item in sub_categories:
        col_sub_categories.insert({'name': item})

    # Update categories with statistics info
    r_categories = col_categories.find({})
    for category in r_categories:
        news_count = col.count({'category': category['name']})
        col_categories.update({'name': category['name']}, {'$set': {'count': news_count}} )

    # r_sub_categories = col_sub_categories.find({})
    # for sub_category in r_sub_categories:
    #     news_count = col.count({'sub_category': sub_categories['name']})
    #     col_categories.update({'name': sub_categories['name']}, {'count': news_count})

def cat_mapping():
    cat_data = [
        {'name': 'Sport', 'labels': ['sports','Sports', 'sport']},
        {'name': 'World', 'labels': ['world']},
        {'name': 'Tech', 'labels': ['Technology', 'tech']},
        {'name': 'Business', 'labels': ['business']},
        {'name': 'Health', 'labels': ['health']},
        {'name': 'Entertainment', 'labels': ['entertainment']},
        {'name': 'Arts', 'labels': ['arts', 'Arts & Culture']},
        {'name': 'Politics', 'labels': ['politics', 'Politics Headlines']},
        {'name': 'Lifestyle', 'labels': ['lifestyle', 'Style', 'Living']},
        {'name': 'U.S', 'labels': ['U.S.', 'US', 'US Headlines', 'U.S.	', 'US News', 'us']},
        {'name': 'Science', 'labels': ['science']},
        {'name': 'Women', 'labels': []},
        {'name': 'Travel', 'labels': ['travel']}
    ]

    # map_rss
    rss = col_rss.find()
    for item in rss:
        for cat in cat_data:
            for label in cat['labels']:
                if item['category'] == label:
                    col_rss.update({'link': item['link']}, {'$set': {'category': cat['name']}})
def news_mapping():
    cat_data = [
        {'name': 'Sport', 'labels': ['sports','Sports', 'sport']},
        {'name': 'World', 'labels': ['world']},
        {'name': 'Tech', 'labels': ['Technology', 'tech']},
        {'name': 'Business', 'labels': ['business']},
        {'name': 'Health', 'labels': ['health']},
        {'name': 'Entertainment', 'labels': ['entertainment']},
        {'name': 'Arts', 'labels': ['arts', 'Arts & Culture']},
        {'name': 'Politics', 'labels': ['politics', 'Politics Headlines']},
        {'name': 'Lifestyle', 'labels': ['lifestyle', 'Style', 'Living']},
        {'name': 'U.S', 'labels': ['U.S.', 'US', 'US Headlines', 'U.S.	', 'US News', 'us']},
        {'name': 'Science', 'labels': ['science']},
        {'name': 'Women', 'labels': []},
        {'name': 'Travel', 'labels': ['travel']}
    ]

    i = 0
    # map_rss
    news = col.find()
    for item in news:
        i += 1
        if i % 1000 == 0:
            print('==================== %s ====================' % i)
        for cat in cat_data:
            for label in cat['labels']:
                if item['category'] == label:
                    print('Updating %s to %s' % (item['category'],cat['name']))
                    col.update({'link': item['link']}, {'$set': {'category': cat['name']}})

def extract_sources():
    rss = col_rss.find()
    source_list = []
    for item in rss:
        if not item['source'] in source_list:
            source_list.append(item['source'])
    for item in source_list:
        col_sources.insert({'name': item, 'selector': ''})
    print(source_list)

def update_source_info():
    sources = col_sources.find()
    for item in sources:
        count = col.count({'source': item['name']})
        col_sources.update({'name': item['name']}, {'$set': {'news_count': count}})
# cat_mapping()

# news_mapping()

# extract_categories()

# extract_sources()

update_source_info()