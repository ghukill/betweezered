# betweezered app views

# generic
import json

# local
import localConfig
from betweezered_app import app


# write crumb
@app.route("{prefix}/helloworld".format(prefix=localConfig.betweezered_app_prefix), methods=['GET', 'POST'])
def helloworld():

	return "Hello World!"




# # testing
# def main():
# 	for tweet in t.stream("library"):
# 		print(tweet["created_at"],tweet['text'])




# if __name__ == '__main__':
# 	main()