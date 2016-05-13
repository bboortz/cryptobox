#!/usr/bin/env python3

from flask import Flask
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
    return jsonify( appconfig.api_to_json() )

@app.route('/api/config')
def api_config():
    return jsonify( appconfig.config_to_json() )

@app.route('/api/file')
def api_test():
    return jsonify( { 'EXAMPLE': 'jooo' } )


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