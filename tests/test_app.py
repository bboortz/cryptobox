

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

    def teardown(self):
        """This method is run once after _each_ test method is executed"""

    def test_slash(self):
        test_app = app.test_client()
        rv = test_app.get('/')
        assert_equal(rv.status_code, 404)
        assert_not_equal(rv.status_code, 201)

    def test_alive(self):
        test_app = app.test_client()
        rv = test_app.get('/alive')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)

    def test_api(self):
        test_app = app.test_client()
        rv = test_app.get('/api')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)

    def test_config(self):
        test_app = app.test_client()
        rv = test_app.get('/api/config')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)

    def test_post_api(self):
        test_app = app.test_client()
        rv = test_app.post('/api/file')
        assert_equal(rv.status_code, 405)
        assert_not_equal(rv.status_code, 201)

    def test_file(self):
        test_app = app.test_client()
        rv = test_app.get('/api/file')
        assert_equal(rv.status_code, 200)
        assert_not_equal(rv.status_code, 201)
