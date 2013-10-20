
import json
try:
     # For Python 3.0 and later
     from urllib.request import urlopen
except ImportError:
     # Fall back to Python 2's urllib2
     from urllib2 import urlopen
import pymongo

# connect to mongo
# connection = pymongo.Connection("mongodb://localhost", safe=True)
connection = pymongo.MongoClient("mongodb://localhost", safe=True)

# get a handle to the reddit database
db=connection.reddit
stories = db.stories

# get the reddit home page
reddit_page = urlopen("http://www.reddit.com/r/technology/.json")

# parse the json into python objects
parsed = json.loads(reddit_page.read())

# iterate through every news item on the page
for item in parsed['data']['children']:
    # put it in mongo
    stories.insert(item['data'])
