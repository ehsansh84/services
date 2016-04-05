__author__ = 'Ehsan'
from pymongo import MongoClient
con = MongoClient()
db = con.services
db_bigtc = con.bigtc
