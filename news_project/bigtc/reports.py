import sys
sys.path.append('/root/ehsan/services')
from public_data import *

col_rss = db['rss']

def rss_statistics():
    rss_list = col_rss.find()
    total_time = 0
    rss_count = len(rss_list)
    for item in rss_list:
        try:
            total_time += item['duration']
        except Exception, ex:
            print(ex.message)
    print(total_time)
    print(rss_count)

rss_statistics()