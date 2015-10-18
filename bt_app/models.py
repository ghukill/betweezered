#bt models

import sqlalchemy

from bt_app import db

from localConfig import logging


# tweet table
class Tweet(db.Model):

	id = db.Column(db.BIGINT(), primary_key=True)
	text = db.Column(db.String(255)) 

	def __init__(self, tweet_dict):
		logging.debug("Working on tweet %s" % tweet_dict['id'])
		self.id = int(tweet_dict['id'])
		self.text = tweet_dict['text']

	def __repr__(self):    	
		return '<{id}>'.format(id=self.id)