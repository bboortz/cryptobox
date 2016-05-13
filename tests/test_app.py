

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
        
    def test_post_file(self):
        json = { 'file': 'lla' }
        rv = self.test_app.post('/api/file', data=json, follow_redirects=False)
        assert_equal(rv.status_code, 201)
        assert_not_equal(rv.status_code, 405)
        assert '"status": "success"' in rv.data        
        
#    rv = self.app.post('/add', data=dict(
#        title='<Hello>',
#        text='<strong>HTML</strong> allowed here'
#    ), follow_redirects=True)
##    assert 'No entries here so far' not in rv.data
 #   assert '&lt;Hello&gt;' in rv.data
 #   assert '<strong>HTML</strong> allowed here' in rv.data
