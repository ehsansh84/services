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

# try:
#     for item in news:
#         if not item['category'] in categories:
#             categories.append(item['category'])
#
#         if not item['sub_category'] in sub_categories:
#             sub_categories.append(item['sub_category'])
#         i += 1
#
#         if i % 1000 == 0:
#             print(i)
# except Exception, e:
#     print(e.message)


# for item in categories:
#     col_categories.insert({'name': item})

r_categories = col_categories.find({})
for category in r_categories:
    news_count = col.count({'category': category['name']})
    print(news_count),
    print(category)