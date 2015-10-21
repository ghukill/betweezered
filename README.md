# betweezered
Application / Ecosystem to filter streaming twitter api, capture, parse, and preserve


## Requirements

* python installs
 * Requires python dev libraries <em>sudo apt-get install python-dev</em>
 * python mysql <em>sudo apt-get install python-mysqldb</em>
 * <em>sudo pip install -r requirements.txt</em>
 * Create MySQL database
  * <em>CREATE DATABASE betweezered</em>
  * <em>CREATE USER 'betweezered'@'localhost' IDENTIFIED BY 'betweezered';</em>
  * <em>GRANT ALL PRIVILEGES ON betweezered . * TO 'betweezered'@'localhost';</em>
 * Create tables via python models
  * 



## Run

### Apache Kafka
* <a href="http://kafka.apache.org/downloads.html">download Apache Kafka</a>

* start Apache Zookeeper
 * <em>nohup bin/zookeeper-server-start.sh config/zookeeper.properties > zookeeper.out &</em>

* start Kafka Server
 * <em>nohup bin/kafka-server-start.sh config/server.properties > kafka_server.out &</em>

* create Kafka topic
 * <em>bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic betweezered</em>


### start capture
* python twitter_capture.py tskafka

### start betweezered app (consumes and archives)
* python runserver.py