
from lib.appconfig import *
from lib.flaskhelper import *
from wtfforms import *
from flask import Blueprint
from flask import jsonify, make_response, request
from flask import render_template



appconfig = AppConfig.create_instance()
blueprint = Blueprint('frontend', __name__, template_folder='templates')



@blueprint.route('/alive', methods=['GET'])
def get_alive():
    return jsonify( { 'alive': 'true' } )

# Define a route for the default URL, which loads the form
@blueprint.route('/', methods=['GET'])
def get_home():
    return render_template('home.html')

# Define a route for the default URL, which loads the form
@blueprint.route('/upload', methods=['GET'])
@crossdomain(origin=appconfig.API_URL)
def get_upload():
    form = UploadForm()
    return render_template('upload.html', api_url=appconfig.API_URL, form=form)
    
# Define a route for the default URL, which loads the form
@blueprint.route('/list', methods=['GET'])
@crossdomain(origin=appconfig.API_URL)
def get_list():
    return render_template('list.html', api_url=appconfig.API_URL)

# Define a route for the default URL, which loads the form
@blueprint.route('/documentation', methods=['GET'])
def get_documentation():
    return render_template('documentation.html')

