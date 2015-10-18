# betweezered app views

# generic
import json
import time

# local
import localConfig
from bt_app import app


# write crumb
@app.route("{prefix}/helloworld".format(prefix=localConfig.betweezered_app_prefix), methods=['GET', 'POST'])
def helloworld():

	return str(time.time())