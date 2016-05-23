#!/usr/bin/env python

import os, sys, inspect

# use this if you want to include modules from a subfolder
def include_module_path(path):
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],path)))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
include_module_path("..")



from lib.appconfig import *
from lib.blueprint_base import blueprint as blueprint_base
from blueprint_frontend import blueprint as blueprint_frontend
from flask import Flask
from flask import jsonify, make_response
from flask_bootstrap import Bootstrap



appconfig = AppConfig.create_instance()
app = Flask(__name__)
app.config.from_object(appconfig.FLASKCONFIG)
app.register_blueprint(blueprint_base)
app.register_blueprint(blueprint_frontend)
Bootstrap(app)



if __name__ == '__main__':
    app.run(host=appconfig.IP, port=appconfig.PORT, threaded=True)