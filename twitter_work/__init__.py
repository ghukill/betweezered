from rq.decorators import job
from redis import Redis

redis_conn = Redis()

# method to work
@job('normal', connection=redis_conn, timeout=5)
def worker(tweet):
	print tweet['text']