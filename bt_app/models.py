#bt models

import json

import sqlalchemy

from bt_app import db

from localConfig import logging


# tweet table
class Tweet(db.Model):

	id = db.Column(db.BIGINT(), primary_key=True)
	text = db.Column(db.String(255)) 
	tweet_json = db.Column(db.Text)
	created_at = db.Column(db.String(255))
	user_name = db.Column(db.String(255)) 
	user_location = db.Column(db.String(255))
	

	def __init__(self, tweet_dict):

		# parse tweet into db		
		self.id = int(tweet_dict['id'])
		self.text = tweet_dict['text']
		self.tweet_json = json.dumps(tweet_dict)
		self.created_at = tweet_dict['created_at']
		self.user_name = tweet_dict['user']['name']
		self.user_location = tweet_dict['user']['location']



	def __repr__(self):    	
		return '<{id}>'.format(id=self.id)