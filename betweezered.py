# betweezered.py
'''
https://github.com/ghukill/betweezered
'''

# generic
import json

# local
import localConfig

# modules
from twarc import Twarc


# global twarc instance
t = Twarc(localConfig.client_key, localConfig.client_secret, localConfig.access_token, localConfig.access_token_secret)


# testing
def main():
	for tweet in t.stream("library"):
		print(tweet["created_at"],tweet['text'])




if __name__ == '__main__':
	main()