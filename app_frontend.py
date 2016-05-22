#!/usr/bin/env python

from flask import Flask
from flask import jsonify, make_response, request, abort
from flask import render_template, url_for, flash, redirect, Markup
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from lib.appconfig import *
from lib.wtfforms import *
from lib.flaskhelper import *
from lib.jsonhelper import dict_to_bytes
from lib.crypt import Crypt
import simplejson as json



appconfig = AppConfig.create_instance()
crypt = Crypt()
app = Flask(__name__)
app.config.from_object(appconfig.FLASKCONFIG)
Bootstrap(app)



# Define a route for the default URL, which loads the form
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

# Define a route for the default URL, which loads the form
@app.route('/upload', methods=['GET'])
@crossdomain(origin=appconfig.API_URL)
def upload():
    form = UploadForm()
    return render_template('upload.html', api_url=appconfig.API_URL, form=form)
    
# Define a route for the default URL, which loads the form
@app.route('/list', methods=['GET'])
@crossdomain(origin=appconfig.API_URL)
def list():
    return render_template('list.html', api_url=appconfig.API_URL)

# Define a route for the default URL, which loads the form
@app.route('/documentation', methods=['GET'])
def documentation():
    return render_template('documentation.html')




@app.route('/alive', methods=['GET'])
def alive():
    return jsonify( { 'alive': 'true' } )


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