from tweetstream import FilterStream
from tweetstream import ConnectionError, AuthenticationError, SampleStream
from couchdbkit import *

# streamer collects tweets of interest and inserts them into a couchdb
# you can follow arrays of people follow=people 
# or arrays of words track=words

#couchdb init
server = Server(uri='http://geopher.net:5984')
db = server.get_db('cfa311')

# words to track
#people = ['cfa311']
words = ['cfa311']

def get_last_tweet_id():
    id = db.view('summary/all_ids', descending=True).first()
    return id['id']
	
def start_stream():
    try:        
		with FilterStream("cfa311", "CodeMonkies", track=words) as stream:
			for tweet in stream:
				print "Got tweet %s from %-16s\t( tweet %d, rate %.1f tweets/sec)" % \
					(tweet["id_str"], tweet["user"]["screen_name"], stream.count, stream.rate ) 
				db[tweet["id_str"]] = dict(tweet)
    except KeyError, e:
		print "KeyError: ", e
		start_stream()
    except ResourceConflict, e:
		print "ResourceConflict: ", e
		start_stream()				
    except ConnectionError, e:
		print "Disconnected from twitter. Reason:", e.reason
        
start_stream()
