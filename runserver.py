# -*- coding: utf-8 -*-

# betweezered twisted server wrapper
from twisted.web.wsgi import WSGIResource
from twisted.web.server import Site
from twisted.internet import reactor, defer
from twisted.internet.task import deferLater, LoopingCall
from twisted.web.server import NOT_DONE_YET
from twisted.web import server, resource
from twisted.python import log

# twarc
from twarc import Twarc

# rq
from rq import Queue
from redis import Redis

# python modules
import json
import logging
import time
import sys
import threading

# local
import localConfig

# import crumb_http flask app
from betweezered_app import app

# import workers
import twitter_kafka

'''
This Twisted Server wraps the following:
	- betweezered_app - Flask app
	- PythonRQ messaging broker
'''

# global twarc instance
t = Twarc(localConfig.client_key, localConfig.client_secret, localConfig.access_token, localConfig.access_token_secret)


# betweezered_app
resource = WSGIResource(reactor, reactor.getThreadPool(), app)
site = Site(resource)

# run as script
if __name__ == '__main__':

	# betweezered_app
	logging.info('''
██████╗ ███████╗████████╗██╗    ██╗███████╗███████╗███████╗███████╗██████╗ ███████╗██████╗ 
██╔══██╗██╔════╝╚══██╔══╝██║    ██║██╔════╝██╔════╝╚══███╔╝██╔════╝██╔══██╗██╔════╝██╔══██╗
██████╔╝█████╗     ██║   ██║ █╗ ██║█████╗  █████╗    ███╔╝ █████╗  ██████╔╝█████╗  ██║  ██║
██╔══██╗██╔══╝     ██║   ██║███╗██║██╔══╝  ██╔══╝   ███╔╝  ██╔══╝  ██╔══██╗██╔══╝  ██║  ██║
██████╔╝███████╗   ██║   ╚███╔███╔╝███████╗███████╗███████╗███████╗██║  ██║███████╗██████╔╝
╚═════╝ ╚══════╝   ╚═╝    ╚══╝╚══╝ ╚══════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝ 
''')

	# betweezered_app
	reactor.listenTCP(localConfig.betweezered_app_port, site, interface="::")
	logging.info("Listening on %s" % localConfig.betweezered_app_port)

	# consume betweezered kafka topic
	lc = LoopingCall(twitter_kafka.TwitterKafkaLooper().consume)
	lc.start(1)

	# fire reactor
	reactor.run()
