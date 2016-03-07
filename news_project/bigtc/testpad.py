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
    for i in range(2524):
        link = str(sheet.cell(i, 2))
        count = col_rss.find({'link': link}).count()
        print(count)
        # if count > 0:
        #     print(link)

import_xls_rss()