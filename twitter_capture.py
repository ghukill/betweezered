# module to connect to twitter stream

import json
import time
import sys

import localConfig
from localConfig import logging
from twarc import Twarc
from twisted.internet import protocol
from twitter_work import tweet_process

# Apache Kafka
from kafka import KafkaClient, SimpleProducer	

# init Kafka
kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
	


#--- Python RQ ---*
class TwitterStreamRQ(object):

	# WORKING TWITTER HOSE
	def __init__(self, search_terms):

		logging.info("initializing TwitterStream RQ")

		# globals to all instances
		self.t = Twarc(localConfig.client_key, localConfig.client_secret, localConfig.access_token, localConfig.access_token_secret)
		self.search_terms = search_terms

	# method to capture twitter stream
	def captureStream(self):
		fhand = open('/tmp/tweet_hose.csv','w')
		for tweet in self.t.stream(",".join(self.search_terms)):
			tweet_process.delay(tweet)
			fhand.write(json.dumps(tweet))
			fhand.write('\n')

		fhand.close()



class LocalStreamRQ(object):

	# LOCAL TWITTER HOSE EMULATOR
	def __init__(self, search_terms):

		logging.info("initializing LocalStream RQ")

		# globals to all instances
		self.search_terms = search_terms
		fhand = open('tests/real_tweets.csv','r')
		self.lt = []
		for line in fhand:
			self.lt.append(json.loads(line))

	# method to capture twitter stream
	def captureStream(self):
		while True:
			logging.debug("sending stream at slight delay")
			for tweet in self.lt:
				tweet_process.delay(tweet)
				time.sleep(.25)


	# method to capture twitter stream
	def burstStream(self):
		logging.debug("sending all local tweets as burst")
		for tweet in self.lt:
			tweet_process.delay(tweet)



#--- Apache Kafka---*
class TwitterStreamKafka(object):

	pass

	# # WORKING TWITTER HOSE
	# def __init__(self, search_terms):

	# 	logging.info("initializing TwitterStream Kafka")

	# 	# globals to all instances
	# 	self.t = Twarc(localConfig.client_key, localConfig.client_secret, localConfig.access_token, localConfig.access_token_secret)
	# 	self.search_terms = search_terms

	# # method to capture twitter stream
	# def captureStream(self):
	# 	fhand = open('/tmp/tweet_hose.csv','w')
	# 	for tweet in self.t.stream(",".join(self.search_terms)):
	# 		tweet_process.delay(tweet)
	# 		fhand.write(json.dumps(tweet))
	# 		fhand.write('\n')

	# 	fhand.close()



class LocalStreamKafka(object):

	# LOCAL TWITTER HOSE EMULATOR
	def __init__(self, search_terms):

		logging.info("initializing LocalStream Kafka")

		# globals to all instances
		self.search_terms = search_terms
		fhand = open('tests/real_tweets.csv','r')
		self.lt = []
		for line in fhand:
			self.lt.append(line)

	# method to capture twitter stream
	def captureStream(self):
		while True:
			logging.debug("sending stream at slight delay")
			for tweet_json in self.lt:
				result = producer.send_messages("betweezered", tweet_json)
				time.sleep(.25)


	# # method to capture twitter stream
	# def burstStream(self):
	# 	logging.debug("sending all local tweets as burst")
	# 	for tweet in self.lt:
	# 		tweet_process.delay(tweet)


def main():

	# grab stream type
	if len(sys.argv) < 2:
		logging.critical("Please enter either 'lt' for local tweets, or 'ts' for live tweets, followed with 'rq' or 'kafka' for capture type.  e.g. 'ltrq' for local, rq capture, or 'tskafka' for live, kafka capture")
	else:
		stream_type = sys.argv[1]

	#--- RQ Capture ---#
	if stream_type == 'tsrq':
		ts = TwitterStreamRQ(localConfig.search_terms)
		ts.captureStream()

	if stream_type == 'ltrq':
		lt = LocalStreamRQ(localConfig.search_terms)
		if sys.argv[2] == "burst":
			lt.burstStream()	
		if sys.argv[2] == "stream":
			lt.captureStream()


	#--- Kafka Capture ---#
	if stream_type == 'tskafka':
		ts = TwitterStreamKafka(localConfig.search_terms)
		ts.captureStream()

	if stream_type == 'ltkafka':
		lt = LocalStreamKafka(localConfig.search_terms)
		if sys.argv[2] == "burst":
			lt.burstStream()	
		if sys.argv[2] == "stream":
			lt.captureStream()


if __name__ == '__main__':
	main()	


	
