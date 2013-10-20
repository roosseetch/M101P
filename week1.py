# -- coding: utf-8 --
import pymongo
import bottle


# this is the handler for the default path of the web server

@bottle.route('/')
def index():

	# connect to MongoDB
	connection = pymongo.MongoClient('localhost', 27017)

	# attache to test database
	db = connection.test

	# get handle for names collection
	names = db.names

	# find single document
	item = names.find_one()

	#return bottle.template('<b>Hello {{name}}</b>!', name=name)
	return '<b>Hello %s</b>!' % item['name']

bottle.run(host='localhost', port=8082, reloader=True)
