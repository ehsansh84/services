import sys
sys.path.append("/root/projects/services")
from public_data import db


col = db['ir_domains_processed']


def check_avail():
    avail_string = 'ERROR:101: no entries found'
    domains = col.find()
    for domain in domains:
        available = avail_string in domain['whois']
        print(available)


check_avail()