import sys
sys.path.append("/root/ehsan/services")
from public_data import *

col = db['news']

categories = []
sub_categories = []

i = 0
news = col.find({})
try:

    for item in news:
        if not item['category'] in categories:
            print(str(i) + 'Cur Cat: %s Cats: %s' % (item['category'], categories))
            categories.append(item['category'])
        # if not item['sub_category'] in sub_categories:
        #     categories.append(item['sub_category'])
        print(i)
        i += 1

        # if i % 1000 == 0:
        #     print(i)
        if i % 10 == 0:
            break
except Exception, e:
    print(e.message)

print('CATS:')
print(categories)
# print('SUB CATS:')
# print(sub_categories)


