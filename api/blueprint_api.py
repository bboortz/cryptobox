from lib.appconfig import *
from lib.applogger import AppLogger
from lib.flaskhelper import *
from lib.pythonversionhelper import str_to_bytes
from lib.jsonhelper import dict_to_bytes, json_to_dict, os_environ_to_dict
from lib.crypt import PassCrypt
from cryptography.fernet import InvalidToken
from flask import Blueprint
from flask import jsonify, make_response, request, abort
from flask import url_for
from flask import current_app





appconfig = AppConfig.create_instance()
LOGGER = AppLogger.create_instance(appconfig=appconfig)
blueprint = Blueprint('api', __name__, template_folder='templates')
crypt = PassCrypt()



db = {}
db_id = 0



@blueprint.route('/alive', methods=['GET'])
@crossdomain(origin='*')
def get_alive():
    return jsonify( { 'alive': 'true' } )

@blueprint.route('/api', methods=['GET'])
@crossdomain(origin='*')
def get_api():
    return jsonify( appconfig.api_to_json() )

@blueprint.route('/api/config', methods=['GET'])
@crossdomain(origin='*')
def api_get_config():
    return jsonify( appconfig.config_to_json() )

if appconfig.ENV == 'DEV':
    @blueprint.route('/api/env', methods=['GET'])
    @crossdomain(origin='*')
    def api_get_env():
        return jsonify( os_environ_to_dict() )

@blueprint.route('/api/file', methods=['GET'])
@crossdomain(origin='*')
def api_get_file():
    return jsonify( db )

@blueprint.route('/api/file/<int:file_id>', methods=['GET'])
@crossdomain(origin='*')
def api_get_file_id(file_id):
    cryptkey = request.headers.get('cryptkey')
    abort_on_zero_string(cryptkey)
        
    file_id_str = str(file_id)
    if not file_id_str in db:
        abort(404)
    
    encoded_cryptkey = str_to_bytes(cryptkey)
    try:
        file = crypt.decrypt(db[file_id_str], encoded_cryptkey)
    except InvalidToken:
        abort(404)
    except ValueError:
        abort(404)
    if file == None  or  file == ""  or  file.__sizeof__() == 0:
        abort(404)
    
    try:
        file_dict = json_to_dict(file)
        return make_response( jsonify( {'file': file_dict } ) , 200 )
    except Exception:
        return make_response( jsonify( {'file': file } ) , 200 )
        
@blueprint.route('/api/file', methods=['POST'])
@crossdomain(origin='*')
def api_post_file():
    global db_id
    item = { "%s" % db_id:  None }
    cryptkey = ""
    
    
    LOGGER.debug( "cryptpass(headers): %s" % request.headers.get('cryptpass') )
    LOGGER.debug( "cryptpass(form): %s" % request.form.get('cryptpass') )
    cryptpass_str = request.form.get('cryptpass')
    if cryptpass_str == None:
        cryptpass_str = request.headers.get('cryptpass')
    abort_on_zero_string(cryptpass_str)
    
    if is_mimetype_json():
        json_dict = request.get_json()
        if json_dict == None:
            abort(401)
        json_bytes=dict_to_bytes(json_dict)
        content, cryptkey = crypt.encrypt(json_bytes, cryptpass_str)
        item = { "%s" % db_id: content }
        
    else:
        content_str=request.form['content']
        abort_on_zero_string(content_str)
        content_bytes = content_str
        content, cryptkey =  crypt.encrypt(content_bytes, cryptpass_str)
        item = { "%s" % db_id:  content }
    
    abort_on_zero_string(cryptkey)
    
    new_id = db_id    
    url = "%s/%d" % (url_for('api.api_get_file', _external=True), new_id)
    db_id += 1
    db.update(item)
    
    return make_response(jsonify({'status': 'success', 'id': str(new_id), 'cryptkey': cryptkey, 'url': url }), 201)

