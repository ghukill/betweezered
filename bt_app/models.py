#bt models

import json
import datetime 

from localConfig import logging

# mongo
from mongoengine import *
connect('twitterapology')

# MongoDB
class MongoTweet(DynamicDocument):
	id = StringField(primary_key=True)
