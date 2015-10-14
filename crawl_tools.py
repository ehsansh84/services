import urllib2


def get_url(url):
    response = urllib2.urlopen(url)
    return response.read()
