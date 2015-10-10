# module to connect to twitter stream
import localConfig
from twarc import Twarc
from twisted.internet import protocol
from twitter_work import worker 

class TwitterStream(object):

	def __init__(self, search_terms):
		# globals to all instances
		self.t = Twarc(localConfig.client_key, localConfig.client_secret, localConfig.access_token, localConfig.access_token_secret)
		self.search_terms = search_terms

	# method to capture twitter stream
	def captureStream(self):		
		for tweet in self.t.stream(",".join(self.search_terms)):
			worker.delay(tweet)		


def main():

	ts = TwitterStream(localConfig.search_terms)
	ts.captureStream()


if __name__ == '__main__':
	main()	


	
