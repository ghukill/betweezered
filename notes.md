#NOTES

##To-Do
	* install flask - sqlalchemy connector
	* reorganize file structure (e.g. twitter_kafka --> betweezer_process, twitter_capture --> betweezer_capture)
	* create 'catch-up' module that performs search (as opposed to listen to stream), to prime or collect missed tweets from past
	* if not running, the consumer does NOT go back and capture finish up things not yet processed.  this is big.	
	* create topics in kafka for topics outline in localConfig


##Rambles
	*Sitting here mulling it over, the hose might not be the right approach.

	*UNLESS, each instance of betweezered can cast a net over a few search terms, 
	these are ALL captured in the same DB.  We could try to guess which term landed it, 
	but maybe we'll not know?  maybe the tweet metadata will include it?  All is not lost.

	*Consider wrapping all this in a supervisor file?

	*Consider removing 'twitter_work', hich is primarily python RQ.  Kafka is great.  Embrace.

	* could pretty easily normalize, but if end goal is spreadsheets, maybe easy to leave flat?

	* put mongo db connection somewhere central, better yet, create models yo!


## Removed from requirements when leaving SQL
sqlalchemy
Flask-SQLAlchemy
* Python MySQLdb drivers
  * <em>sudo apt-get install python-mysqldb</em>
* Create MySQL database
  * <em>CREATE DATABASE betweezered</em>
  * <em>CREATE USER 'betweezered'@'localhost' IDENTIFIED BY 'betweezered';</em>
  * <em>GRANT ALL PRIVILEGES ON betweezered . * TO 'betweezered'@'localhost';</em>
* Create tables via python models
  * <em>python create_tables.py</em>
