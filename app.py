#!/usr/bin/env python3

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





appconfig = AppConfig.create_instance()
crypt = Crypt()


app = Flask(__name__)
app.config.from_object(appconfig.FLASKCONFIG)
Bootstrap(app)



# Define a route for the default URL, which loads the form
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', result=db)

# Define a route for the default URL, which loads the form
@app.route('/upload', methods=['GET'])
def upload():
    form = UploadForm()
    
    return render_template('upload.html', form=form)
    
# Define a route for the default URL, which loads the form
@app.route('/list', methods=['GET'])
def list():
    return render_template('list.html', result=db)

# Define a route for the default URL, which loads the form
@app.route('/documentation')
def documentation():
    return render_template('documentation.html', result=db)




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
    file_id_str = str(file_id)
    if not file_id_str in db:
        abort(404)
    
    file = crypt.decrypt(db[file_id_str])
    if file == None  or  file == ""  or  file.__sizeof__() == 0:
        abort(404)
    
    return make_response( jsonify( {'file': file } ) , 200 )
    
db = {}
db_id = 0
@app.route('/api/file', methods=['POST'])
def api_post_file():
    global db_id
    item = { "%s" % db_id:  None }
    form = UploadForm()

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
    url = "%s/%d" % (url_for('api_get_file', _external=True), new_id)
    db_id += 1
    db.update(item)
    
    if form.validate_on_submit():
        message = Markup("You have successfully uploaded the content! Access url: <a href='%s'>%s</a>" % (url,url) )
        flash(message)
        return redirect(url_for('upload'))
    
    return make_response(jsonify({'status': 'success', 'id': str(new_id), 'url': url }), 201)


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