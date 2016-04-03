import sys
import re
sys.path.append("/root/ehsan/services")
from public_data import *
import xlrd
import xlsxwriter
from tools import *
from bs4 import BeautifulSoup
import urllib2
import cookielib
col = db['news']
col_temp = db['temp']
col_sources = db['sources']


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


def mark_news_as_unknown():
    cats = ['Latest Stories', 'Top Stories', 'Latest Headlines', 'Most Recent', 'News', 'All News', 'World Headlines', 'Most Popular', 'All of CNET', 'Latest News', 'hot news', 'CNET News']
    news = col.find()
    i = 1
    for item in news:
        if item['category'] in cats:
            col.update({'link': item['link']}, {'$set': {'category': 'Unknown'}})
            print('Updated')
        i += 1
        if i % 2000 == 0:
            print(40 * '='),
            print(i)


def add_empty_selector_field_to_sources():
    sources = col_sources.find()
    for item in sources:
        col_sources.update({'name': item['name']}, {'$set': {'selector': ''}})
        print('Updated')


def add_empty_exclude_field_to_sources():
    sources = col_sources.find()
    for item in sources:
        col_sources.update({'name': item['name']}, {'$set': {'exclude': ''}})
        print('Updated')


def news_text_fetch():
    sources = col_sources.find()
    for source in sources:
        selector = source['selector']
        if selector != '':
            unread_news_count = col.count({'source': source['name'], 'text': ''})
            # unread_news_count = col.count({'source': source['name'], 'text': '', 'category': {'$ne': 'Unknown'}})
            log.color_print(color=Color.LIME, text='Source is: {} and unread news count is: {}'.format(source['name'], unread_news_count))
            news = col.find({'source': source['name'], 'text': ''})
            i = 0
            for item in news:
                try:
                    link = item['link']
                    # log.color_print(color=Color.BLUE, text=link)
                    doc = urllib2.urlopen(link)
                    # soup = BeautifulSoup(str(doc).lower(), 'html.parser')
                    soup = BeautifulSoup(doc, 'html.parser')
                    # log.color_print(color=Color.YELLOW, text=selector)
                    # log.color_print(color=Color.YELLOW, text='div[itemprop="articleBody"]')
                    # news_area = soup.select(selector)
                    # news_area = soup.select('div[itemprop="articleBody"]')[0]
                    news_area = soup.select(selector)[0]
                    # log.color_print(color=Color.CYAN, text=news_area)
                    for script in news_area(["script", "style"]):
                        script.extract()
                    # print(news_area.text)
                    col.update({'link': link}, {'$set': {'text': news_area.text}})
                    i += 1
                    # log.color_print(color=Color.RED, text=40 * '=')
                    if i % 100 == 0:
                        log.color_print(color=Color.YELLOW, text=i)
                except Exception, e:
                    log.color_print(color=Color.RED, text=e.message)

def news_text_fetch_v2():
    sources = col_sources.find()
    for source in sources:
        selector = source['selector']
        if selector != '':
            unread_news_count = col.count({'source': source['name'], 'text': ''})
            log.color_print(color=Color.LIME, text='Source is: {} and unread news count is: {}'.format(source['name'], unread_news_count))
            news = col.find({'source': source['name'], 'text': ''})
            i = 0
            for item in news:
                try:
                    link = item['link']
                    cj = cookielib.CookieJar()
                    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
                    request = urllib2.Request(link)
                    doc = opener.open(request)
                    soup = BeautifulSoup(doc, 'html.parser')
                    # log.color_print(color=Color.YELLOW, text=selector)
                    # log.color_print(color=Color.BLUE, text=link)
                    # log.color_print(color=Color.YELLOW, text='div[itemprop="articleBody"]')
                    # news_area = soup.select(selector)
                    # log.color_print(color=Color.LIME, text=news_area)
                    news_area = soup.select(selector)[0]
                    for exclude_item in source['exclude']:
                        for div in news_area.select(exclude_item):
                            div.extract()
                    for script in news_area(["script", "style"]):
                        script.extract()
                    col.update({'link': link}, {'$set': {'text': news_area.text}})
                    i += 1
                    if i % 100 == 0:
                        log.color_print(color=Color.YELLOW, text=i)
                except:
                    log.color_print(color=Color.RED, text=log.get_exception())


def news_text_fetch_test_one():
    try:
        link = 'http://cityroom.blogs.nytimes.com/2015/10/20/grieving-with-a-firefighter/?_r=0'
        # selector = '#js-article-text > div:nth-child(8)'
        try:
            # doc = urllib2.urlopen(link)
            import cookielib, urllib2
            cj = cookielib.CookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            request = urllib2.Request(link)
            doc = opener.open(request)
        except Exception, e:
            print(e.args)
            print(e)
            log.color_print(color=Color.CYAN, text=e.message)

        soup = BeautifulSoup(doc, 'html.parser')
        # log.color_print(color=Color.CYAN, text=soup)
        news_area = soup.select('div[class="entry-content"]')[0]
        log.color_print(color=Color.RED, text=news_area)
        for div in news_area.select('div[class=\"inlineModule\"]'):
            div.extract()
        for script in news_area(["script", "style"]):
            script.extract()
        # news_text = BeautifulSoup(news_area, 'html.parser')
        # print(len(news_area))
        # print(news_area.text)
        log.color_print(color=Color.LIME, text=news_area.text.encode('utf-8'))
    except Exception, e:
        # print('Error:'),
        # print(e.args),
        log.color_print(color=Color.RED, text=log.get_exception())



def create_temp_bigtc_dataset():
    col = db['news']
    db_bigtc = con.bigtc
    col_news = db_bigtc['news']
    news = col.find({'text': {'$ne': ''}, 'category': {'$ne': 'Unknown'}})
    for item in news:
        col_news.insert(item)


def create_output_excel():
    try:
        workbook = xlsxwriter.Workbook('output/results.xls')
        worksheet = workbook.add_worksheet('Step1')
        row = 2

        worksheet.write('A1', 'ID')
        worksheet.write('B1', 'CLASS')
        worksheet.write('C1', 'TEXT')

        news = col.find({'category': {'$ne': 'Unknown'}, 'text': {'$ne': ''}}).limit(10)
        for item in news:
            worksheet.write('A' + str(row), str(item['_id']))
            worksheet.write('B' + str(row), item['category'])
            worksheet.write('C' + str(row), item['text'])
            row += 1

        workbook.close()
    except:
        log.color_print(color=Color.RED, text=log.get_exception())

# create_temp_bigtc_dataset()
create_output_excel()
# news_text_fetch()
# news_text_fetch_v2()
# news_text_fetch_test_one()
# backup_news()
# mark_news_as_unknown()
# add_empty_selector_field_to_sources()
# add_empty_exclude_field_to_sources()

