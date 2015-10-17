# betweezered
Application / Ecosystem to filter streaming twitter api, capture, parse, and preserve


## Installation
* We'll get there...


## Run
* Star consumer: `rqworker normal`
	** `rqworker normal` must be run from root directory of project 
* Start listener: `python twitter_capture.py`
* Start webapp: `python runserver.py`


'''
Sitting here mulling it over, the hose might not be the right approach.

UNLESS, each instance of betweezered can cast a net over a few search terms, 
these are ALL captured in the same DB.  We could try to guess which term landed it, 
but maybe we'll not know?  maybe the tweet metadata will include it?  All is not lost.

Consider wrapping all this in a supervisor file?
'''