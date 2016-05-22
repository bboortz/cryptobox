#!/usr/bin/env python

import os, sys, inspect

# use this if you want to include modules from a subfolder
def include_module_path(path):
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],path)))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
include_module_path("api")



from lib.appconfig import *
from api.blueprint_api import blueprint as blueprint_api
from frontend.blueprint_frontend import blueprint as blueprint_frontend
from flask import Flask
from flask import jsonify, make_response
from flask_bootstrap import Bootstrap



appconfig = AppConfig.create_instance()
app = Flask(__name__)
app.config.from_object(appconfig.FLASKCONFIG)
app.register_blueprint(blueprint_api)
app.register_blueprint(blueprint_frontend)
Bootstrap(app)



@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
    
@app.errorhandler(405)
def method_not_allowed(error):
    return make_response(jsonify({'error': 'Method Not Allowed'}), 405)

@app.errorhandler(500)
def internal_error(error):
    return make_response(jsonify({'error': 'Unexpected Server Error'}), 500)


if __name__ == '__main__':
    app.run(host=appconfig.IP, port=appconfig.PORT, threaded=True)
