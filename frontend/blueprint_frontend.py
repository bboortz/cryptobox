
from lib.appconfig import *
from lib.flaskhelper import *
from wtfforms import *
from flask import Blueprint
from flask import jsonify, make_response, request
from flask import render_template, url_for, flash
from flask_wtf import Form
import simplejson as json



appconfig = AppConfig.create_instance()
blueprint = Blueprint('frontend', __name__, template_folder='templates')



@blueprint.route('/alive', methods=['GET'])
def alive():
    return jsonify( { 'alive': 'true' } )

# Define a route for the default URL, which loads the form
@blueprint.route('/', methods=['GET'])
def home():
    return render_template('home.html')

# Define a route for the default URL, which loads the form
@blueprint.route('/upload', methods=['GET'])
@crossdomain(origin=appconfig.API_URL)
def upload():
    form = UploadForm()
    return render_template('upload.html', api_url=appconfig.API_URL, form=form)
    
# Define a route for the default URL, which loads the form
@blueprint.route('/list', methods=['GET'])
@crossdomain(origin=appconfig.API_URL)
def list():
    return render_template('list.html', api_url=appconfig.API_URL)

# Define a route for the default URL, which loads the form
@blueprint.route('/documentation', methods=['GET'])
def documentation():
    return render_template('documentation.html')

