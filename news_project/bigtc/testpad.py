import sys
import re
sys.path.append("/root/ehsan/services")
from public_data import *
col = db['news']
results = col.find({}).limit(100)
for r in results:
    # print(r['title'])
    summary = r['summary']
    summary = re.sub("<.*?>", "", summary)
    print(summary)