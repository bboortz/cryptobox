
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
    
    return_url = request.form.get('return_url')
    url = request.form.get('url')
    id = request.form.get('id')
    cryptkey = request.form.get('cryptkey')
    
    abort_on_zero_string(return_url)
    abort_on_zero_string(url)
    abort_on_zero_string(id)
    abort_on_zero_string(cryptkey)
    
    form = ResultForm(id, url, cryptkey)
    
    return render_template('uploadresult.html', api_url=appconfig.API_URL, form=form, return_url=return_url, url=url, id=id, cryptkey=cryptkey)

# Define a route for the default URL, which loads the form
@blueprint.route('/accesscontent', methods=['GET'])
@crossdomain(origin=appconfig.API_URL)
def get_accesscontent():
    form = AccessForm()
    print appconfig.API_URL
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

# Define a route for the default URL, which loads the form
#@blueprint.route('/js/<path:path>', methods=['GET'])
#def get_js(path):
#    mimetype = "application/javascript"
#    return send_from_directory(directory='frontend/static/js', filename=path, mimetype=mimetype)

