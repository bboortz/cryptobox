
from lib.appconfig import *
from lib.applogger import AppLogger
from lib.flaskhelper import *
from wtfforms import *
from flask import Blueprint
from flask import jsonify, make_response, request, send_from_directory
from flask import render_template



appconfig = AppConfig.create_instance()
LOGGER = AppLogger.create_instance(appconfig=appconfig)
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
@blueprint.route('/uploadresult', methods=['POST'])
@crossdomain(origin=appconfig.API_URL)
def get_uploadresult():
    print(request.form)
    
    freturn_url = request.form.get('return_url')
    furl = request.form.get('url')
    fid = request.form.get('id')
    fcryptkey = request.form.get('cryptkey')
    
    abort_on_zero_string(freturn_url)
    abort_on_zero_string(furl)
    abort_on_zero_string(fid)
    abort_on_zero_string(fcryptkey)
    
    form = ResultForm(fid, furl, fcryptkey)
    
    return render_template('uploadresult.html', api_url=appconfig.API_URL, form=form, return_url=freturn_url, url=furl, id=fid, cryptkey=fcryptkey)

# Define a route for the default URL, which loads the form
@blueprint.route('/accesscontent', methods=['GET'])
@crossdomain(origin=appconfig.API_URL)
def get_accesscontent():
    form = AccessForm()
    return render_template('accesscontent.html', api_url=appconfig.API_URL, form=form)

# Define a route for the default URL, which loads the form
@blueprint.route('/list', methods=['GET'])
@crossdomain(origin=appconfig.API_URL)
def get_list():
    return render_template('list.html', api_url=appconfig.API_URL)

# Define a route for the default URL, which loads the form
@blueprint.route('/documentation', methods=['GET'])
def get_documentation():
    return render_template('documentation.html')
