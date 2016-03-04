import sys
import re
sys.path.append("/root/ehsan/services")
from public_data import *
col = db['news']
results = col.find({}).limit(100)
output = open('output.txt', 'w')

for r in results:
    # print(r['title'])
    summary = r['summary']
    summary = re.sub("<.*?>", "", summary)
    print(summary)
    output.write(summary.encode('utf-8'))
output.close()