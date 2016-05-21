#!/usr/bin/env python3

from flask import Flask
from flask import jsonify, make_response, request, abort
from lib.appconfig import *
from lib.crypt import Crypt



appconfig = AppConfig.create_instance()
crypt = Crypt()


app = Flask(__name__)
app.config.from_object(appconfig.FLASKCONFIG)


@app.route('/alive', methods=['GET'])
def alive():
    return jsonify( { 'alive': 'true' } )

@app.route('/api', methods=['GET'])
def api():
    return jsonify( appconfig.api_to_json() )

@app.route('/api/config', methods=['GET'])
def api_get_config():
    return jsonify( appconfig.config_to_json() )

@app.route('/api/file', methods=['GET'])
def api_get_file():
    return jsonify( db )

@app.route('/api/file/<int:file_id>', methods=['GET'])
def api_get_file_id(file_id):
    global db

    file_id_str = str(file_id)
    if not file_id_str in db:
        abort(404)
    
    file = crypt.decrypt(db[file_id_str])
    if file == None:
        abort(404)
    
    return make_response( jsonify( {'file': file } ) , 200 )
    
db = {}
db_id = 0
@app.route('/api/file', methods=['POST'])
def api_post_file():
	global db
	global db_id
	
	json_str = str(request.json)
	json_bytes = json_str.encode()
	content =  crypt.encrypt(json_bytes)
	
	item = { "%s" % db_id:  content }
	db_id += 1
	db.update(item)
	return make_response(jsonify({'status': 'success', 'id': str(db_id-1) }), 201)


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