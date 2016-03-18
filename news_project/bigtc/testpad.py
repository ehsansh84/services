import sys
import re
sys.path.append("/root/ehsan/services")
from public_data import *
import xlrd

col = db['news']
col_temp = db['temp']

def extract_summaries():
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


def import_xls_rss():
    xl_workbook = xlrd.open_workbook('rss.xls')
    sheet_names = xl_workbook.sheet_names()
    sheet = xl_workbook.sheet_by_name(sheet_names[0])
    col_rss = db['rss']
    rss_new = 0
    rss_dup = 0

    for i in range(1,2524):
        link = str(sheet.cell(i, 2))[7:-1]
        source = str(sheet.cell(i, 1))[7:-1]
        catrgory = str(sheet.cell(i, 4))[7:-1]
        country = str(sheet.cell(i, 0))[7:-1]
        # if source == 'cnn':
        #     print(link)
        # print(source)

        if country == 'usa':
            count = col_rss.find({'link': link}).count()
            if count == 0:
                rss_new += 1
                col_rss.insert({
                    'category': catrgory,
                    'sub_category': [],
                    'source': source,
                    'link': link,
                    'active': 1,
                    'handy': 0
                })
                print(catrgory)
                print(count)
            else:
                rss_dup += 1
            # if count > 0:
            #     print(link)
    print('NEW: %s DUP: %s' % (rss_new, rss_dup))

import_xls_rss()
