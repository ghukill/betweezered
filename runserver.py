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

# python modules
import json
import logging
import time
import sys
import threading

# local
import localConfig

# import crumb_http flask app
from bt_app import app

# import workers
import bt_kafka


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
	if localConfig.ts_kafka_consume == True:
		lc = LoopingCall(bt_kafka.TwitterKafkaLooper().consume)
		lc.start(localConfig.ts_kafka_loop_delay)

	# fire reactor
	reactor.run()
