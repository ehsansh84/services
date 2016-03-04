from public_data import *
col = db['news']
results = col.find({}).limit(100)
for r in results:
    print(r['title'])