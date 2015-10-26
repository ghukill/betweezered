# betweezered
Application / Ecosystem to filter streaming twitter api, capture, parse, and preserve


## Requirements

* Install Apache Kafka
  * <a href="http://kafka.apache.org/downloads.html">download Apache Kafka</a>
* Python dev libraries
  * `sudo apt-get install python-dev`
* Install requirements via pip
  * `sudo pip install -r requirements.txt`


## Run

Betweezered runs with the help of supervisor, which starts the following:<br>
* Apache Zookeeper
* Apache Kafka server
* Twitter Stream capture (twitter_capture.py)
* Betweezered Server

`<em>supervisord -c sup_conf.conf</em>`

Betweezered's components can be viewed with the supervisor web console at: `localhost:9001`
