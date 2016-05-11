#!/usr/bin/env python
#!flask/bin/python
import sys
import os
from flask import Flask, __version__
from flask import jsonify, make_response
from lib.appconfig import *



appconfig = AppConfig.create_instance()


app = Flask(__name__)
app.config.from_object(appconfig.FLASKCONFIG)


@app.route('/alive')
def alive():
    return jsonify( { 'alive': 'true' } )

@app.route('/api')
def api():
    return jsonify( { 'api': appconfig.APPNAME, 'api-version': appconfig.APPVERSION, 'flask-version': __version__ } )

@app.route('/api/file')
def api_test():
    return jsonify( { 'api': appconfig.APPNAME, 'api-version': appconfig.APPVERSION, 'flask-version': __version__ } )

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def internal_error(error):
    return make_response(jsonify({'error': 'Unexpected Server Error'}), 500)



if __name__ == '__main__':
    app.run(host=appconfig.IP, port=appconfig.PORT, threaded=True)