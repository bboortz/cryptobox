

from app import app
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
        
    def test_post_file0(self):
        json = { 'file': 'lla' }
        rv = self.test_app.post('/api/file', data=json, follow_redirects=False)
        assert_equal(rv.status_code, 201)
        assert_not_equal(rv.status_code, 405)
        assert '"id": "0"' in str(rv.data)
        assert '"status": "success"' in str(rv.data)
        
        
    def test_post_file1_and_get(self):
        json = "{ 'KEY': 'VALUE' }"
        rv = self.test_app.post('/api/file', data=json, follow_redirects=False)
        assert_equal(rv.status_code, 201)
        assert_not_equal(rv.status_code, 405)
        assert '"id": "1"' in str(rv.data)
        assert '"status": "success"' in str(rv.data)
        
        rv = self.test_app.get('/api/file/1')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)
        
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
        

        