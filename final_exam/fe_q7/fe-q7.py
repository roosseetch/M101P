# -*- coding: utf-8 -*-
import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost", safe=True)

# get a handle to the school database
db = connection.photobase

albums = db.albums
images = db.images


def full_album():

	try:
		albums_cursor = albums.find({}, {'_id': 0, 'images': 1})

	except:
		print("Unexpected error:", sys.exc_info()[0])

	full_al = set([])

	for images_coll in albums_cursor:
		full_al.update(set(images_coll['images']))

	return full_al


def all_images():

	try:
		images_cursor = images.find({}, {'_id': 1})

	except:
		print("Unexpected error:", sys.exc_info()[0])

	all_im = set([])

	for image in images_cursor:
		all_im.add(image['_id'])

	return all_im


def orphan_images(collect1, collect2):
	collect1.difference_update(collect2)
	return collect1


def remove_orphans(orphans):

	print("start removing ...")

	for id in orphans:
		images.remove({"_id": id})


print("There are 49,932 images that are tagged 'kittens' before you remove the images.\n\
	And You have %d elements." % images.find({'tags': 'kittens'}).count())

# remove_orphans(orphan_images(all_images(), full_album()))
full_album = full_album()
images_remove = images.remove
num_images = images.count()
images_cursor = images.find({}, {'_id': 1})
print("start removing ...")
# [images_remove({"_id": id}) for id in range(num_images) if id not in full_album]
[images_remove({"_id": image['_id']}) for image in images_cursor if image['_id'] not in full_album]

print("Should be 89,737 documents in the images collection.\n\
	And You have %d elements." % images.count())

print("Images that are tagged 'kittens' after removal is %d" % images.find({'tags': 'kittens'}).count())
