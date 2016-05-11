
from lib.appconfig import AppConfig
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises


class TestAppConfig(object):
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

    def test_create_instance_default(self):
        appconfig = AppConfig.create_instance()
        assert_equal(appconfig.ENV, os.getenv('ENV', 'PROD'))
        assert_not_equal(appconfig.ENV, "QA")
        
    def test_create_instance_prod(self):
        appconfig = AppConfig.create_instance("PROD")
        assert_equal(appconfig.ENV, "PROD")
        assert_not_equal(appconfig.ENV, "QA")
        
    def test_create_instance_qa(self):
        appconfig = AppConfig.create_instance("QA")
        assert_equal(appconfig.ENV, "PROD")
        assert_not_equal(appconfig.ENV, "QA")
        
    def test_create_instance_test(self):
        appconfig = AppConfig.create_instance("TEST")
        assert_equal(appconfig.ENV, "TEST")
        assert_not_equal(appconfig.ENV, "QA")
        
    def test_create_instance_dev(self):
        appconfig = AppConfig.create_instance("DEV")
        assert_equal(appconfig.ENV, "DEV")
        assert_not_equal(appconfig.ENV, "QA")
