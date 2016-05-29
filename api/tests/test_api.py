
import os, sys, inspect

# use this if you want to include modules from a subfolder
def include_module_path(path):
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],path)))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
include_module_path("..")


from lib.pythonversionhelper import isinstance_of_string
from lib.jsonhelper import dict_to_json, json_to_dict
from app_api import app, appconfig
from nose.tools import assert_equal
from nose.tools import assert_not_equal



class TestApp(object):

    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""
        

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        #app['TESTING'] = True
        self.test_app = app.test_client()

    def teardown(self):
        """This method is run once after _each_ test method is executed"""

    def test_get_slash(self):
        rv = self.test_app.get('/')
        assert_equal(rv.status_code, 404)
        assert_not_equal(rv.status_code, 201)
        
    def test_get_alive(self):
        rv = self.test_app.get('/alive')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)

    def test_get_api(self):
        rv = self.test_app.get('/api')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)
        
    def test_post_api(self):
        rv = self.test_app.post('/api')
        assert_equal(rv.status_code, 405)
        assert_not_equal(rv.status_code, 201)
        
    def test_post_api_api(self):
        rv = self.test_app.post('/api/api')
        assert_equal(rv.status_code, 404)
        assert_not_equal(rv.status_code, 201)

    def test_get_config(self):
        rv = self.test_app.get('/api/config')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)
        
    def test_get_env(self):
        rv = self.test_app.get('/api/env')
        if appconfig.ENV == 'DEV':
            assert_equal(rv.status_code, 200)
        else:
            assert_equal(rv.status_code, 404)
        assert_not_equal(rv.status_code, 201)

    def test_get_file(self):
        rv = self.test_app.get('/api/file')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)
        
    def test_get_file_wrong_id(self):
        cryptkey='TESTKEY'
        headers = [('cryptkey', cryptkey)]
        rv = self.test_app.get('/api/file/1000', headers=headers)
        assert_equal(rv.status_code, 404)
        assert_not_equal(rv.status_code, 200)
        
    def test_get_file_wrong_cryptkey(self):
        cryptkey='TESTKEY'
        headers = [('cryptkey', cryptkey)]
        rv = self.test_app.get('/api/file/0', headers=headers)
        assert_equal(rv.status_code, 404)
        assert_not_equal(rv.status_code, 200)
        
        content='beispiel text 123'
        cryptpass='TESTKEY'
        headers = [('cryptpass', cryptpass)]
        data = dict(content=content)
        rv = self.test_app.post('/api/file', data=data , headers=headers, follow_redirects=False)
        
        assert_equal(rv.status_code, 201)
        assert_not_equal(rv.status_code, 405)
        assert '"id": "0"' in str(rv.data)
        assert '"status": "success"' in str(rv.data)
        
        data = json_to_dict( rv.data.decode() )
        id = data['id']
        cryptkey = data['cryptkey']
        assert_equal(isinstance_of_string(cryptkey), True)
        assert_not_equal(isinstance_of_string(cryptkey), False)
        assert_not_equal(cryptkey, "")
        
        headers = [('cryptkey', cryptkey.upper() )]
        rv = self.test_app.get("/api/file/" + id, headers=headers)
        assert_equal(rv.status_code, 404)
        assert_not_equal(rv.status_code, 201)

    def test_get_file_without_cryptkey(self):
        rv = self.test_app.get('/api/file/0')
        assert_equal(rv.status_code, 400)
        assert_not_equal(rv.status_code, 200)
        
    def test_get_file_alphabetical(self):
        rv = self.test_app.get('/api/file/abcd')
        assert_equal(rv.status_code, 404)
        assert_not_equal(rv.status_code, 200)
        
    def test_post_file0_text(self):
        content='beispiel text 123'
        cryptpass='TESTKEY'
        headers = [('cryptpass', cryptpass)]
        data = dict(content=content)
        rv = self.test_app.post('/api/file', data=data , headers=headers, follow_redirects=False)
        
        assert_equal(rv.status_code, 201)
        assert_not_equal(rv.status_code, 405)
        assert '"id": "1"' in str(rv.data)
        assert '"status": "success"' in str(rv.data)
        
        data = json_to_dict( rv.data.decode() )
        id = data['id']
        cryptkey = data['cryptkey']
        assert_equal(isinstance_of_string(cryptkey), True)
        assert_not_equal(isinstance_of_string(cryptkey), False)
        assert_not_equal(cryptkey, "")
        
        headers = [('cryptkey', cryptkey)]
        rv = self.test_app.get("/api/file/" + id, headers=headers)
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)
        print(rv.data)
        
        data = json_to_dict( rv.data.decode() )
        assert_equal(data['file'], 'beispiel text 123')
        
        
        
    def test_post_file0_text_wrong_form(self):
        data = dict(wrongkey='data1')
        rv = self.test_app.post('/api/file', data=data , follow_redirects=False)
        assert_equal(rv.status_code, 400)
        assert_not_equal(rv.status_code, 405)
        
    def test_post_file0_text_none(self):
        rv = self.test_app.post('/api/file', data=None , follow_redirects=False)
        assert_equal(rv.status_code, 400)
        assert_not_equal(rv.status_code, 405)
        
    def test_post_file0_text_empty(self):
        data = dict(content='')
        rv = self.test_app.post('/api/file', data=data , follow_redirects=False)
        assert_equal(rv.status_code, 400)
        assert_not_equal(rv.status_code, 405)
    
    def test_post_file1_json(self):
        cryptpass='TESTKEY'
        headers = [('Content-Type', 'application/json'), ('cryptpass', cryptpass)]
        data = {'name': 'Jessy', 'testcase': 'test_post_file1_and_get'}
        json_data = dict_to_json(data)
        json_data_length = len(json_data)
        headers.append(('Content-Length', json_data_length))
        rv = self.test_app.post('/api/file', data=json_data, headers=headers, follow_redirects=False)
        
        assert_equal(rv.status_code, 201)
        assert_not_equal(rv.status_code, 405)
        assert '"id": "2"' in str(rv.data)
        assert '"status": "success"' in str(rv.data)
        
        data = json_to_dict( rv.data.decode() )
        id = data['id']
        cryptkey = data['cryptkey']
        assert_equal(isinstance_of_string(cryptkey), True)
        assert_not_equal(isinstance_of_string(cryptkey), False)
        assert_not_equal(cryptkey, "")
        
        headers = [('Content-Type', 'application/json'), ('cryptkey', cryptkey)]
        rv = self.test_app.get('/api/file/' + id, headers=headers)
        
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)
        data = json_to_dict( rv.data.decode() )
        #file_dict = json.loads(data['file'])
        assert_equal(data['file']['name'], 'Jessy')
        
    
    def test_post_file1_fake_json(self):
        headers = [('Content-Type', 'application/json')]
        json_data = "FAKE JSON"
        json_data_length = len(json_data)
        headers.append(('Content-Length', json_data_length))
        rv = self.test_app.post('/api/file', data=json_data, headers=headers, follow_redirects=False)
        assert_equal(rv.status_code, 400)
        assert_not_equal(rv.status_code, 405)
        
    def test_post_file1_None_json(self):
        headers = [('Content-Type', 'application/json')]
        json_data = "FAKE JSON"
        json_data_length = len(json_data)
        headers.append(('Content-Length', json_data_length))
        rv = self.test_app.post('/api/file', data=None, headers=headers, follow_redirects=False)
        assert_equal(rv.status_code, 400)
        assert_not_equal(rv.status_code, 405)
       
    def test_unknown_function(self):
        rv = self.test_app.delete('/api/file/0', follow_redirects=False)
        assert_equal(rv.status_code, 405)
        assert_not_equal(rv.status_code, 200)

 