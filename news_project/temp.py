import hashlib
import redis

# print(hashlib.algorithms_available)
# print(hashlib.algorithms_guaranteed)
# hash_object = hashlib.md5('Hello World')

# print(hash_object.hexdigest())

# m = hashlib.md5()
# m.update("Hello world")
# print m.hexdigest()

# redis_server = redis.Redis('localhost')
# redis_server.set('ehsan', '25')
# print(redis_server.get('ehsan'))
#
# redis_server.set('age', 10)
# redis_server.incr('age')
# redis_server.decr('age')
# print(redis_server.get('age'))


from pymongo import MongoClient
from datetime import datetime, timedelta

con = MongoClient()
db_bigtc = con.bigtc
col_rss = db_bigtc['rss']
d = (datetime.now() - timedelta(hours=4))
# d1 = (datetime.now() - timedelta(hours=10))
rss_links = col_rss.count({'last_read': {'$gt':  d}})
# print(d1)
# rss_links = col_rss.count({'last_read': {'$lt':  'ISODate("2016-05-18T15:38:56.847Z")'}})
# rss_links = col_rss.count({'last_read': {'$gt':  ISODATE('2016-05-18T15:28:20.927Z')}})
print(d)
print(rss_links)


# from datetime import datetime, timedelta

