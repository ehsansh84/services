__author__ = 'Ehsan'
import sys
sys.path.append("/root/ehsan/services")
from public_data import *
import feedparser
# import rss_data
# from rss_data import rss_links
from tools import timer
from datetime import  datetime

# print(str(sys.argv))
# try:
#     s = sys.argv[1]
# except:
#     pass
# print(s)
# exit()


col_news = db['news']
col_rss = db['rss']
col_rss_log = db['rss_log']
t = timer()

# col_rss = db['rss']
# for item in rss_links:
#     item['handy'] = 1
#     item['active'] = 1
#     col_rss.insert(item)
# exit()




from lxml import etree
parser = etree.HTMLParser()
tree = etree.parse("http://www.dailymail.co.uk/sport/football/article-3437261/Real-Madrid-just-11-fans-attend-win-Granada-Spanish-averse-travelling-away-games.html?ITO=1490&ns_mchannel=rss&ns_campaign=1490", parser)
print(tree)
cells = tree.xpath("//*[@id='js-article-text']/div[2]")
print(cells)
# for td in cells:
#     if td.attrib.has_key('class') and td.attrib['class'].find('highlight') != -1:
#         print(tr.text)