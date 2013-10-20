# -*- coding: utf-8 -*-
import pymongo
# import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.blog
posts = db.posts


# cursor = posts.find().limit(4)

# for post in cursor:
	# post['date'] = post['date'].strftime("%A, %B %d %Y at %I:%M%p") # fix up date
	# print(post['date'])
	# print(post['date'])
	# print(post[0])

def get_posts(num_posts):

	cursor = []         # Placeholder so blog compiles before you make your changes

	# XXX HW 3.2 Work here to get the posts
	cursor = posts.find().sort('date', pymongo.DESCENDING).limit(num_posts)
	# cursor = posts.find().limit(num_posts)
	# cursor.append(posts.find().limit(num_posts))
	l = []

	for post in cursor:
		post['date'] = post['date'].strftime("%A, %B %d %Y at %I:%M%p")    # fix up date
		if 'tags' not in post:
			post['tags'] = [] # fill it in if its not there already
	if 'comments' not in post:
			post['comments'] = []

	l.append({'title':post['title'], 'body':post['body'], 'post_date':post['date'],
		'permalink':post['permalink'],
		'tags':post['tags'],
		'author':post['author'],
		'comments':post['comments']})

	return l, len(l)

# print(get_posts(3))

def lasterr():
	# return db.runCommand({ 'getLastError': 1})
	# db.write_concern['comment'] = 'How can I Fly in the Sky ???'
	return db.write_concern['n']

print(lasterr())
# print(lasterr()())
