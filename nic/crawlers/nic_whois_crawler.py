from public_data import db
from crawl_tools import get_url
from bs4 import BeautifulSoup


col = db['ir_domains']
col_processed = db['ir_domains_processed']

domains = col.find()
domain_count = col.count()
i = 0
for domain in domains:
    if i % 1000 == 0:
        print(i)
    whois = ''
    try:
        print(domain['domain'])
        link = "http://whois.nic.ir/WHOIS?name=%s.ir" % domain['domain']
        print(link)
        html = get_url(link)
        soap = BeautifulSoup(html, "html.parser")
        try:
            whois = soap.select(selector='pre')
        except Exception, e:
            print('*************ERROR*****************')
            print(e.message)
    except Exception, e:
        print('*******************')
        print(e.message)
        print('Error in domain: ' + domain['domain'])
    col.remove({'domain': domain['domain']})
    col_processed.insert({'domain': domain['domain'], 'whois': str(whois), 'available': 'x'})
    i += 1

