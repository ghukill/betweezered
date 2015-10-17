# module to connect to twitter stream

import json
import time
import sys

import localConfig
from localConfig import logging
from twarc import Twarc
from twisted.internet import protocol
from twitter_work import tweet_process 



class TwitterStream(object):

	# WORKING TWITTER HOSE
	def __init__(self, search_terms):

		logging.info("initializing TwitterStream")

		# globals to all instances
		self.t = Twarc(localConfig.client_key, localConfig.client_secret, localConfig.access_token, localConfig.access_token_secret)
		self.search_terms = search_terms

	# method to capture twitter stream
	def captureStream(self):		
		for tweet in self.t.stream(",".join(self.search_terms)):
			tweet_process.delay(tweet)



class LocalStream(object):

	# LOCAL TWITTER HOSE EMULATOR
	def __init__(self, search_terms):

		logging.info("initializing LocalStream")

		# globals to all instances
		self.search_terms = search_terms
		lt = open('tests/local_tweets.json','r')
		self.lt = json.loads(lt.read())

	# method to capture twitter stream
	def captureStream(self):
		while True:
			logging.debug("sending another set")
			for tweet in self.lt:
				tweet_process.delay(tweet)
			time.sleep(1)


def main():

	# grab stream type
	if len(sys.argv) < 2:
		stream_type = 'lt'
	else:
		stream_type = sys.argv[1]

	if stream_type == 'ts':
		ts = TwitterStream(localConfig.search_terms)
		ts.captureStream()
	if stream_type == 'lt':
		lt = LocalStream(localConfig.search_terms)
		lt.captureStream()	


if __name__ == '__main__':
	main()	


	
