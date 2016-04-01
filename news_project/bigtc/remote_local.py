from pymongo import MongoClient

local_con = MongoClient()
# remote_con = MongoClient('37.59.92.3', 27017)
remote_con = MongoClient('37.59.92.3:27017')

local_db = local_con.bigtc
remote_db = remote_con.bigtc

local_news = local_db['news']
remote_news = remote_db['news']

data = remote_news.find()
for item in data:
    local_news.insert(item)