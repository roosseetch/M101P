# -*- coding: utf-8 -*-
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost", safe=True)

# get a handle to the school database
db = connection.school
students = db.students


def remove_bad_homework():

	print("find, reporting for duty")

	try:
		# num_students = students.count() // students.find({'_id': 0}).count()
		num_students = students.count()

	except:
		print("Unexpected error:", sys.exc_info()[0])


	num_students = students.count()

	for student in range(num_students):

		'''
		score = students.find({'_id': student}, {'scores': 1, '_id': 0})[0]['scores'] is array
		for example for
		> students.find({'_id': 100}, {'scores': 1, '_id': 0})[0]['scores']

		score is

		[ { "type" : "exam", "score" : 47.42608580155614 },
		{ "type" : "quiz", "score" : 44.83416623719906 },
		{ "type" : "homework", "score" : 19.85604968544429 },
		{ "type" : "homework", "score" : 39.01726616178844 } ]

		here score[2] is
		> students.find({'_id': 100}, {'scores': 1, '_id': 0})[0]['scores'][2]
		{ "type" : "homework", "score" : 19.85604968544429 }

		therefore score[2]['score'] is
		> students.find({'_id': 100}, {'scores': 1, '_id': 0})[0]['scores'][2]['score']
		19.85604968544429

		and score[3]['score'] is
		> students.find({'_id': 100}, {'scores': 1, '_id': 0})[0]['scores'][3]['score']
		39.01726616178844
		'''
		score = students.find({'_id': student}, {'scores': 1, '_id': 0})[0]['scores']

		howework_score_min = score[2]['score']
		if score[2]['score'] > score[3]['score']:
			howework_score_min = score[3]['score']

		students.update( {'_id': student}, { '$pull': { 'scores': {'score': howework_score_min }}})

remove_bad_homework()

# for student in range(5):

# 	score = students.find({'_id': student}, {'scores': 1, '_id': 0})[0]['scores']
# 	howework_score_min = score[2]['score']

# 	print(howework_score_min)
