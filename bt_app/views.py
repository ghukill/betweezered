# betweezered app views

# generic
import json
import time

from flask import jsonify, render_template

# local
import localConfig
from bt_app import app, models

# return json for tweet
@app.route("{prefix}/tweets/<limit>".format(prefix=localConfig.betweezered_app_prefix), methods=['GET', 'POST'])
def tweet(limit):

	# return tweet json
	tweets = models.MongoTweet.objects().limit(int(limit))
	return render_template('tweets.htm',tweets=tweets)
