#crumb_kafka

# python module
from localConfig import logging
import json

# apache kafka
from kafka import KafkaConsumer

# bt_app
from bt_app import db, models


# kafka consumer
class TwitterKafkaLooper(object):
	
	def __init__(self):
		try:
			self.consumer = KafkaConsumer("betweezered",
									  group_id="betweezered_consumer",
									  metadata_broker_list=["localhost:9092"])
			logging.info("Initialized Apache Kafka connection.")
		except:
			logging.warning("Could not initialize Apache Kafka connection.")


	def consume(self):
		messages = self.consumer.fetch_messages()
		for message in messages:
			logging.debug("Kafka message received")
			result = self.processMessage(message)


	# process message from consumer
	def processMessage(self, message):

		try:
			# retrieve payload and parse
			payload = json.loads(message.value)
			logging.info("tweet text: %s" % payload['text'])

			# insert into MySQL
			try:
				t = models.Tweet(payload)
				db.session.add(t)
				db.session.commit()
				logging.debug("tweet inserted into db, id %s" % t.id)
			except Exception, e:
				db.session.rollback()
				logging.warning("COULD NOT INSERT INTO DB.  Error: %s" % 	e)


		except Exception, e:
			logging.warning(e)
			# flush session

