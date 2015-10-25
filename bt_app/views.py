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

	renderdict = {}

	# return tweet json
	renderdict['tweets'] = models.MongoTweet.objects().limit(int(limit))
	renderdict['count'] = models.MongoTweet.objects.count()
	renderdict['limit'] = limit

	# add search terms
	renderdict['search_terms'] = localConfig.search_terms

	return render_template('tweets.htm',renderdict=renderdict)
