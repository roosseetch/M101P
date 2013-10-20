# -- coding: utf-8 --
# import pymongo
from pymongo import MongoClient

# connect database
connection = MongoClient('localhost', 27017)

db = connection.test

# handle to names collection
names = db.names

item = names.find_one()

print(item['name'])
