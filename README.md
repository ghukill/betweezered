# betweezered
Application / Ecosystem to filter streaming twitter api, capture, parse, and preserve


## Installation
* 



## Run

### Apache Kafka
* <a href="http://kafka.apache.org/downloads.html">download Apache Kafka</a>

* start Apache Zookeeper
** <em>nohup bin/zookeeper-server-start.sh config/zookeeper.properties > zookeeper.out &</em>

* start Kafka Server
** <em>nohup bin/kafka-server-start.sh config/server.properties > kafka_server.out &</em>

* create Kafka topic
** <em>bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic betweezered</em>

### Start Betweezered App
*A thing here...