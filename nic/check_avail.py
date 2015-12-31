import sys
sys.path.append("/root/ehsan/services")
from public_data import db


col = db['ir_domains_processed']
col2 = db['ir_domains_processed2']


def check_avail():
    i = 0
    avail_string = 'ERROR:101: no entries found'
    domains = col.find()
    for domain in domains:
        available = avail_string in domain['whois']
        domain['available'] = available
        col2.insert(domain)
        if i % 100 == 0:
            print(i)
        i += 1
        # print(domain['domain'] + ':' + str(available))

check_avail()
