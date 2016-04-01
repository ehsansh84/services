import sys
sys.path.append('/root/ehsan/services')
from public_data import *

col_rss = db['rss']

def rss_statistics():
    rss_list = col_rss.find()
    total_time = 0

    rss_count = col_rss.count()
    rss_active_count = col_rss.count({'active': 1})
    rss_active_duration = 0
    rss_inactive_count = col_rss.count({'active': 0})
    rss_inactive_duration = 0
    for item in rss_list:
        try:
            total_time += item['duration']
            if item['active'] == 1:
                rss_active_duration += item['duration']
            else:
                rss_inactive_duration += item['duration']

        except Exception, ex:
            print(ex.message)
    print('RSS count: %s - Active: Count=>%s Duration=> %s - Inactive: Count=>%s Duration %s' % (
        rss_count, rss_active_count, rss_active_duration , rss_inactive_count, rss_inactive_duration
    ))

def rss_list():
    rss_list = col_rss.find().sort([('duration', -1)])

    for item in rss_list:
        try:
            print('Duration: %s Link: %s' % (item['duration'], item['link']))
        except:
            print('ERROR')




# rss_statistics()

# rss_list()