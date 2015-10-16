# module to connect to twitter stream

import json
import time
import sys

import localConfig
from twarc import Twarc
from twisted.internet import protocol
from twitter_work import worker 


class TwitterStream(object):

	# WORKING TWITTER HOSE
	def __init__(self, search_terms):

		# globals to all instances
		self.t = Twarc(localConfig.client_key, localConfig.client_secret, localConfig.access_token, localConfig.access_token_secret)
		self.search_terms = search_terms

	# method to capture twitter stream
	def captureStream(self):		
		for tweet in self.t.stream(",".join(self.search_terms)):
			worker.delay(tweet)



class LocalStream(object):

	# LOCAL TWITTER HOSE EMULATOR
	def __init__(self, search_terms):

		# globals to all instances
		self.search_terms = search_terms
		lt = open('local_tweets.json','r')
		self.lt = json.loads(lt.read())

	# method to capture twitter stream
	def captureStream(self):
		while True:
			print "Sending a round!"		
			for tweet in self.lt:
				worker.delay(tweet)
			time.sleep(3)


def main():

	stream_type = sys.argv[1]
	if stream_type == 'ts':
		ts = TwitterStream(localConfig.search_terms)
		ts.captureStream()
	if stream_type == 'lt':
		lt = LocalStream(localConfig.search_terms)
		lt.captureStream()	


if __name__ == '__main__':
	main()	


	
