#crumb_kafka

# python module
import logging
import json

# apache kafka
from kafka import KafkaConsumer


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
			logging.info("Kafka message received: {msg}".format(msg=message))
			result = self.processMessage(message)


	# process message from consumer
	def processMessage(self, message):

		try:
			# retrieve payload and parse
			payload = json.loads(message.value)
			logging.debug(payload)

		except Exception, e:
			crumb_handle.release_crumb_lock()
			logging.debug(str(e))
			return str(e)
