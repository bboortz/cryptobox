
from lib.appconfig import *
from flask import Blueprint
from flask import jsonify, make_response



appconfig = AppConfig.create_instance()
blueprint = Blueprint('base', __name__, template_folder='templates')



@blueprint.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)
    
@blueprint.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@blueprint.errorhandler(405)
def method_not_allowed(error):
    return make_response(jsonify({'error': 'Method Not Allowed'}), 405)

#@blueprint.errorhandler(500)
#def internal_error(error):
#    return make_response(jsonify({'error': 'Unexpected Server Error'}), 500)
