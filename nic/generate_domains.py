import sys
sys.path.append("/root/ehsan/services")
from public_data import db


col = db['ir_domains']

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def alpha3_domains():
    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                col.insert({'domain': a+b+c, 'whois': '', 'available': '', 'type': 'alpha3'})


def x4y_domains():
    for a in alphabet:
        for b in alphabet:
            col.insert({'domain': a+'4'+b, 'whois': '', 'available': '', 'type': 'x4y'})
            col.insert({'domain': a+'0'+b, 'whois': '', 'available': '', 'type': 'x0y'})


def xiya_domains():
    for a in alphabet:
        for b in alphabet:
            col.insert({'domain': a+'i'+b+'a', 'whois': '', 'available': '', 'type': 'xiya'})
            col.insert({'domain': a+'a'+b+'i', 'whois': '', 'available': '', 'type': 'xayi'})
            col.insert({'domain': a+'a'+b+'a', 'whois': '', 'available': '', 'type': 'xaya'})
            col.insert({'domain': a+'i'+b+'i', 'whois': '', 'available': '', 'type': 'xiyi'})
            col.insert({'domain': a+'e'+b+'e', 'whois': '', 'available': '', 'type': 'xeye'})
            col.insert({'domain': a+'e'+b+'a', 'whois': '', 'available': '', 'type': 'xeya'})
            col.insert({'domain': a+'a'+b+'e', 'whois': '', 'available': '', 'type': 'xaye'})


def trip_domains():
    for a in alphabet:
        col.insert({'domain': a+'trip', 'whois': '', 'available': '', 'type': 'atrip'})
        col.insert({'domain': 'trip'+a, 'whois': '', 'available': '', 'type': 'tripa'})

def news_domains():
    list = []
    keywords = ['on', 'my', 'we', 'me', 'you', 'pub', 'cast', 'broad']
    for c in alphabet:
        list.append(c + 'news')
        list.append('news' + c)

    for k in keywords:
        list.append(k + 'news')
        list.append('news' + k)

    for c in alphabet:
        list.append(c + 'khabar')
        list.append('khabar' + c)

    for k in keywords:
        list.append(k + 'khabar')
        list.append('khabar' + k)


# alpha3_domains()
# x4y_domains()
# xiya_domains()
# trip_domains()

news_domains()