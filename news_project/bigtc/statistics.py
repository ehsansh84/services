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
try:

    for item in news:
        if not item['category'] in categories:
            categories.append(item['category'])

        if not item['sub_category'] in sub_categories:
            sub_categories.append(item['sub_category'])
        i += 1

        if i % 1000 == 0:
            print(i)
        # if i % 10000 == 0:
        #     break
except Exception, e:
    print(e.message)

print('CATS:')
print(categories)

for item in categories:
    col_categories.insert({'name': item})


# print('SUB CATS:')
# print(sub_categories)


