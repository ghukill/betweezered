# module for processing tweets as consumed by RQ




from rq.decorators import job
from redis import Redis
from localConfig import logging

'''
This component consumes tweets via rq in Redis, and does something with them
'''

redis_conn = Redis()


# method to work
@job('normal', connection=redis_conn, timeout=5)
def tweet_process(tweet):
	logging.info("TWEET TEXT: %s" % tweet['text'])