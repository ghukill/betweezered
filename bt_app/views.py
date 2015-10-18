# betweezered app views

# generic
import json
import time

from flask import jsonify

# local
import localConfig
from bt_app import app, models

# return json for tweet
@app.route("{prefix}/tweet/<id>".format(prefix=localConfig.betweezered_app_prefix), methods=['GET', 'POST'])
def tweet(id):

	# return tweet json
	tweet = models.Tweet.query.filter_by(id=id).first()
	return jsonify(**json.loads(tweet.tweet_json))
