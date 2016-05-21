

from app import app
from nose.tools import assert_equal
from nose.tools import assert_not_equal
import json


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
        assert_equal(rv.status_code, 200)
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

    def test_get_file(self):
        rv = self.test_app.get('/api/file')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)
        
    def test_get_file_wrong(self):
        rv = self.test_app.get('/api/file/1000')
        assert_equal(rv.status_code, 404)
        assert_not_equal(rv.status_code, 200)
        
    def test_post_file0_text(self):
        data = dict(content='beispiel text 123')
        rv = self.test_app.post('/api/file', data=data , follow_redirects=False)

        assert_equal(rv.status_code, 201)
        assert_not_equal(rv.status_code, 405)
        assert '"id": "0"' in str(rv.data)
        assert '"status": "success"' in str(rv.data)
        
        rv = self.test_app.get('/api/file/0')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)
        print(rv.data)
        
        data = json.loads( str(rv.data) )
        assert_equal(data['file'], 'beispiel text 123')
        
        
    def test_post_file0_text_wrong_form(self):
        
        data = dict(wrongkey='data1')
        rv = self.test_app.post('/api/file', data=data , follow_redirects=False)

        assert_equal(rv.status_code, 400)
        assert_not_equal(rv.status_code, 405)
        
    
    def test_post_file1_json(self):
        headers = [('Content-Type', 'application/json')]
        data = {'name': 'Jessy', 'testcase': 'test_post_file1_and_get'}
        json_data = json.dumps(data)
        json_data_length = len(json_data)
        headers.append(('Content-Length', json_data_length))
        rv = self.test_app.post('/api/file', data=json_data, content_type = 'application/json', headers=headers, follow_redirects=False)
        assert_equal(rv.status_code, 201)
        assert_not_equal(rv.status_code, 405)
        assert '"id": "1"' in str(rv.data)
        assert '"status": "success"' in str(rv.data)
        
        rv = self.test_app.get('/api/file/1', content_type = 'application/json', headers=headers)
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)
        data = json.loads( rv.data )
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
       
        
    def test_unknown_function(self):
        rv = self.test_app.delete('/api/file/0', follow_redirects=False)
        assert_equal(rv.status_code, 405)
        assert_not_equal(rv.status_code, 200)



#    def test_post_none_file(self):
#        json = None
#        rv = self.test_app.post('/api/file', data=None, follow_redirects=False)
#        rv = self.test_app.post('/api/file', follow_redirects=False)
#        assert_equal(rv.status_code, 400)
#        assert_not_equal(rv.status_code, 401)
        

        