import sys
import re
sys.path.append("/root/ehsan/services")
from public_data import *
import xlrd
from bs4 import BeautifulSoup
import urllib2
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

# import_xls_rss()

def backup_news():
    news = col.find()
    col_news_backup = db['news_backup_2016-04-01']
    i = 1
    for item in news:
        col_news_backup.insert(item)
        i += 1
        if i % 2000 == 0:
            print(i)

def news_text_fetch():
    link = 'http://www.dailymail.co.uk/sport/football/article-3437261/Real-Madrid-just-11-fans-attend-win-Granada-Spanish-averse-travelling-away-games.html?ITO=1490&ns_mchannel=rss&ns_campaign=1490'
    # selector = '#js-article-text > div:nth-child(8)'
    doc = urllib2.urlopen(link)
    soup = BeautifulSoup(doc, 'html.parser')
    news_area = soup.select('div[itemprop="articleBody"]')[0]
    for script in news_area(["script", "style"]):
        script.extract()
    # news_text = BeautifulSoup(news_area, 'html.parser')
    # print(len(news_area))
    print(news_area.text)

# news_text_fetch()
backup_news()