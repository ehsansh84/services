import sys
sys.path.append("/root/ehsan/services")
from public_data import *

col = db['news']

categories = []
sub_categories = []

i = 0
news = col.find({})
for item in news:
    if not item['category'] in categories:
        categories.append(item['category'])
    if not item['sub_category'] in sub_categories:
        categories.append(item['sub_category'])
    i += 1
    if i % 1000 == 0:
        print(i)
    if i % 10000 == 0:
        break

print('CATS:')
print(categories)
print('SUB CATS:')
print(sub_categories)


