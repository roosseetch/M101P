# -*- coding: utf-8 -*-
import pymongo
import sys
from bson.objectid import ObjectId

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost", safe=True)

# get a handle to the school database
db = connection.students
grades = db.grades


def remove_bad_homework():

	print("find, reporting for duty")

	try:
		num_students = grades.count() // grades.find({'student_id': 0}).count()

	except:
		print("Unexpected error:", sys.exc_info()[0])

	query = {'type': 'homework'}

	ids = []
	for i in range(num_students):
		try:
			query['student_id'] = i
			cursor = grades.find(query).sort('score', pymongo.ASCENDING).limit(1)[0]
			ids.append(cursor['_id'])

		except:
			print("Unexpected error:", sys.exc_info()[0])

	for id in ids:
		grades.remove({"_id": ObjectId(id)})

remove_bad_homework()

print(grades.count())
