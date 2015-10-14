# This bit searches for all 3 char .ir domains and stores in a collection
__author__ = 'Ehsan'
import urllib2
from bs4 import BeautifulSoup
from pymongo import MongoClient
con = MongoClient()
t = con.NIC.tika
tu = con.NIC.tika_updated

def get_url(url):
    response = urllib2.urlopen(url)
    return response.read()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def make_domains():
    for a in alphabet:
        for b in alphabet:
            t.insert({'domain': a + 'i' + b + 'a', 'whois': '', 'available': ''})
# make_domains()
whois = ''
domains = t.find()
for domain in domains:
    # try:
    print(domain['domain'])
    link = "http://whois.nic.ir/WHOIS?name=%s.ir" % domain['domain']
    print(link)
    html =get_url(link)
    soap = BeautifulSoup(html, "html.parser")
    # try:
    whois = soap.select(selector='pre')
    # except Exception, e:
    #     print('*************ERROR*****************')
    #     print(e.message)
    # except Exception, e:
    #     print('*******************')
    #     print(e.message)
    #     print('Error in domain: ' + domain['domain'])
    # print('whois:'),
    # print(whois)
    # t.update({'domain': domain['domain']}, {'whois': str(whois), 'available': 'x'})
    print({'domain': domain['domain']})
    t.remove({'domain': domain['domain']})
    tu.insert({'domain': domain['domain'], 'whois': str(whois), 'available': 'x'})
    # time.sleep(2)


# make_domains()
# crawler(source_links=source_links)
#
