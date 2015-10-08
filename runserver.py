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
from rq import Queue, Connection, Worker

# python modules
import json
import logging
import time
import sys

# local
import localConfig

# import crumb_http flask app
from betweezered_app import app

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
	print '''
██████╗ ███████╗████████╗██╗    ██╗███████╗███████╗███████╗███████╗██████╗ ███████╗██████╗ 
██╔══██╗██╔════╝╚══██╔══╝██║    ██║██╔════╝██╔════╝╚══███╔╝██╔════╝██╔══██╗██╔════╝██╔══██╗
██████╔╝█████╗     ██║   ██║ █╗ ██║█████╗  █████╗    ███╔╝ █████╗  ██████╔╝█████╗  ██║  ██║
██╔══██╗██╔══╝     ██║   ██║███╗██║██╔══╝  ██╔══╝   ███╔╝  ██╔══╝  ██╔══██╗██╔══╝  ██║  ██║
██████╔╝███████╗   ██║   ╚███╔███╔╝███████╗███████╗███████╗███████╗██║  ██║███████╗██████╔╝
╚═════╝ ╚══════╝   ╚═╝    ╚══╝╚══╝ ╚══════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝ 
'''

	# betweezered_app
	reactor.listenTCP(localConfig.betweezered_app_port, site, interface="::")
	print "Listening on",localConfig.betweezered_app_port

	# looping listener for rq consumer
	# with Connection():
	# 	qs = map(Queue, sys.argv[1:]) or [Queue()]
	# 	w = Worker(qs)
	# 	lc = LoopingCall(w.work())
	# 	lc.start(.1)

	# fire reactor
	reactor.run()
