import sys
import re
sys.path.append("/root/ehsan/services")
from public_data import *
col = db['news']
col_temp = db['temp']
results = col.find({}).limit(100)
output = open('output.txt', 'w')
data = ''
for r in results:
    # print(r['title'])
    summary = r['summary']
    summary = re.sub("<.*?>", "", summary)
    print(summary)
    output.write(summary.encode('utf-8'))
    output.write('\n')
    data += summary.encode('utf-8') + '\n'
output.close()
col_temp.insert({'data': data})
