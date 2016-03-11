import sys
sys.path.append("/root/ehsan/services")
from public_data import *

col = db['news']
col_statistics = db['statistics']
col_categories = db['categories']
col_sub_categories = db['sub_categories']

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
