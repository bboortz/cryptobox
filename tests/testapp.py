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
from lib.flaskhelper import *
from flask import Flask
from flask import jsonify



appconfig = AppConfig.create_instance()
app = Flask(__name__)
app.config.from_object(appconfig.FLASKCONFIG)



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
    return jsonify( { 'status': 'green' } )

if __name__ == '__main__':
    app.run(host=appconfig.IP, port=appconfig.PORT, threaded=True)