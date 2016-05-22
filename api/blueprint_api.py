import os
from lib.appconfig import *
from lib.flaskhelper import *
from lib.jsonhelper import dict_to_bytes
from lib.crypt import Crypt
from flask import Blueprint
from flask import jsonify, make_response, request, abort
from flask import url_for
import simplejson as json



appconfig = AppConfig.create_instance()
blueprint = Blueprint('api', __name__, template_folder='templates')
crypt = Crypt()



db = {}
db_id = 0



@blueprint.route('/alive', methods=['GET'])
@crossdomain(origin='*')
def alive():
    return jsonify( { 'alive': 'true' } )

@blueprint.route('/api', methods=['GET'])
@crossdomain(origin='*')
def api():
    return jsonify( appconfig.api_to_json() )

@blueprint.route('/api/config', methods=['GET'])
@crossdomain(origin='*')
def api_get_config():
    return jsonify( appconfig.config_to_json() )
    
@blueprint.route('/api/env', methods=['GET'])
@crossdomain(origin='*')
def api_get_env():
    return jsonify( os.environ )

@blueprint.route('/api/file', methods=['GET'])
@crossdomain(origin='*')
def api_get_file():
    return jsonify( db )

@blueprint.route('/api/file/<int:file_id>', methods=['GET'])
@crossdomain(origin='*')
def api_get_file_id(file_id):
    file_id_str = str(file_id)
    if not file_id_str in db:
        abort(404)
    
    file = crypt.decrypt(db[file_id_str])
    if file == None  or  file == ""  or  file.__sizeof__() == 0:
        abort(404)
    
    try:
        file_dict = json.loads(file)
        return make_response( jsonify( {'file': file_dict } ) , 200 )
    except Exception:
        return make_response( jsonify( {'file': file } ) , 200 )
        
@blueprint.route('/api/file', methods=['POST'])
@crossdomain(origin='*')
def api_post_file():
    global db_id
    item = { "%s" % db_id:  None }
    #form = UploadForm()

    if is_mimetype_json():
        json_dict = request.get_json()
        if json_dict == None:
            abort(400)
        json_bytes=dict_to_bytes(json_dict)
        content = crypt.encrypt(json_bytes)
        item = { "%s" % db_id: content }
        
    else:
        content_str=request.form['content']
        if content_str == None  or  content_str == ""  or  content_str.__sizeof__() == 0:
            abort(400)
        content_bytes = content_str.encode()
        content =  crypt.encrypt(content_bytes)
        item = { "%s" % db_id:  content }
        
    new_id = db_id    
    url = "%s/%d" % (url_for('api.api_get_file', _external=True), new_id)
    db_id += 1
    db.update(item)
    
    return make_response(jsonify({'status': 'success', 'id': str(new_id), 'url': url }), 201)

