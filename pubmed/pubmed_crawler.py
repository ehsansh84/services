import sys
sys.path.append("/root/projects/services")
from public_data import db
from crawl_tools import get_url
from bs4 import BeautifulSoup







col = db['pubmed_articles']
# col_processed = db['ir_domains_processed']

# link = 'http://www.ncbi.nlm.nih.gov/pubmed/?term=article'
rource_link = 'http://www.ncbi.nlm.nih.gov/pubmed/?term=cancer'







doc = get_url(rource_link)
doc = BeautifulSoup(doc, "html.parser")
links = doc.select('.rprt')
for link in links:
    print()
print(len(links))
# links =
# domains = col.find()
# domain_count = col.count()
# i = 0
# for domain in domains:
#     if i % 100 == 0:
#         print(i)
#     whois = ''
#     try:
#         # print(domain['domain'])
#         link = "http://whois.nic.ir/WHOIS?name=%s.ir" % domain['domain']
#         # print(link)
#         html = get_url(link)
#         soap = BeautifulSoup(html, "html.parser")
#         try:
#             whois = soap.select(selector='pre')
#         except Exception, e:
#             print('*************ERROR*****************')
#             print(e.message)
#     except Exception, e:
#         print('*******************')
#         print(e.message)
#         print('Error in domain: ' + domain['domain'])
#     col.remove({'domain': domain['domain']})
#     col_processed.insert({'domain': domain['domain'], 'whois': str(whois), 'available': 'x'})
#     i += 1
#
