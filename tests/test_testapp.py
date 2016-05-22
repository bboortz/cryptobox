
import os, sys, inspect

# use this if you want to include modules from a subfolder
def include_module_path(path):
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],path)))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
include_module_path("..")



from testapp import app
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

    def test_get_origin_star(self):
        rv = self.test_app.get('/get_origin_star')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)
        
    def test_get_origin_star2(self):
        rv = self.test_app.get('/get_origin_star2')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)
        
    def test_get_origin_star3(self):
        rv = self.test_app.get('/get_origin_star3')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)
        
    def test_options_automatic_options(self):
        rv = self.test_app.options('/options_automatic_options')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)
        
    def test_options_not_automatic_options(self):
        rv = self.test_app.options('/options_not_automatic_options')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)
   
    def test_get_origin_api_url(self):
        rv = self.test_app.get('/get_origin_api_url')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)
        
    def test_post_origin_api_url(self):
        data = dict(content='beispiel text 123')
        rv = self.test_app.post('/post_origin_api_url', data=data , follow_redirects=False)
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 405)
        