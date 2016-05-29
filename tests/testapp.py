#!/usr/bin/env python

import os, sys, inspect

# use this if you want to include modules from a subfolder
def include_module_path(path):
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],path)))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
include_module_path("..")
include_module_path("..")



from lib.appconfig import *
from lib.applogger import AppLogger
from lib.jsonhelper import *
from lib.flaskhelper import *
from lib.blueprint_base import blueprint as blueprint_base
from flask import Flask
from flask import abort, jsonify



appconfig = AppConfig.create_instance()
LOGGER = AppLogger.create_instance(appconfig=appconfig)
app = Flask(__name__)
app.config.from_object(appconfig.FLASKCONFIG)
app.register_blueprint(blueprint_base)



@app.route('/get_origin_star', methods=['GET'])
@crossdomain(origin='*', attach_to_all=False)
def get_origin_star():
    return jsonify( { 'status': 'green' } )
    
@app.route('/get_origin_star2', methods=['GET', 'OPTIONS'])
@crossdomain(origin=['www.google.com', 'google.com'], methods=['GET', 'OPTIONS'], headers='Content-Type')
def get_origin_star2():
    return jsonify( { 'status': 'green' } )
    
@app.route('/get_origin_star3', methods=['GET', 'OPTIONS'])
@crossdomain(origin='www.google.de', methods=['GET', 'OPTIONS'], headers='Content-Type')
def get_origin_star3():
    return jsonify( { 'status': 'green' } )
    
@app.route('/options_automatic_options', methods=['OPTIONS'])
@crossdomain(origin='*', methods=['OPTIONS'], automatic_options=True)
def options_automatic_options():
    return jsonify( { 'status': 'green' } )
    
@app.route('/options_not_automatic_options', methods=['OPTIONS'])
@crossdomain(origin='*', methods=['OPTIONS'], automatic_options=False)
def options_not_automatic_options():
    return jsonify( { 'status': 'green' } )
    
@app.route('/get_origin_api_url', methods=['GET'])
@crossdomain(origin=appconfig.API_URL)
def get_origin_api_url():
    return jsonify( { 'status': 'green' } )
    
@app.route('/post_origin_api_url', methods=['POST'])
@crossdomain(origin=appconfig.API_URL, methods=['POST'])
def post_origin_api_url():
    content_str=request.form.get('content')
    
    if content_str == None  or  content_str == ""  or  content_str.__sizeof__() == 0:
        abort(400)
        
    return jsonify( { 'status': 'green' } )
    
@app.route('/get_jsonify', methods=['GET'])
def get_jsonify():
    return jsonify( { 'status': 'green' } )
    
@app.route('/get_jsonify_environ', methods=['GET'])
def get_jsonify_environ():
    env = os_environ_to_dict()
    LOGGER.debug(type(env))
    LOGGER.debug(dir(env))
    LOGGER.debug(os.environ.keys())
    #env_dict = json_to_dict(env)
    #abort(400)
    return jsonify( env )

if __name__ == '__main__':
    app.run(host=appconfig.IP, port=appconfig.PORT, threaded=True)