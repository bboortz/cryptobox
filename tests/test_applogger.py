import os
import logging 
from lib.appconfig import *
from lib.applogger import AppLogger
from nose.tools import assert_equal
from nose.tools import assert_not_equal


class TestAppConfig(object):
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        self.prodconfig = AppConfig.create_instance('PROD')
        self.testconfig = AppConfig.create_instance('TEST')
        self.devconfig = AppConfig.create_instance('DEV')
        self.currentconfig = AppConfig.create_instance()

    def teardown(self):
        """This method is run once after _each_ test method is executed"""
        
    def test_create_instance(self):
        applogger = AppLogger.create_instance()
        currentLogLevel = logging.getLevelName( applogger.log.getEffectiveLevel() )
        applogger.warn("if you see this, this testcase probably failed.")
        assert_equal(applogger.log.name, __name__)
        assert_not_equal(applogger.log.name, "applogger")
        assert_equal(currentLogLevel , 'INFO')
        assert_not_equal(currentLogLevel , 'DEBUG')
        
    def test_create_instance_with_name(self):
        applogger = AppLogger.create_instance(__name__)
        currentLogLevel = logging.getLevelName( applogger.log.getEffectiveLevel() )
        applogger.warn("if you see this, this testcase probably failed.")
        applogger.warn("logging module name: %s" % applogger.log.name)
        assert_equal(applogger.log.name, __name__)
        assert_not_equal(applogger.log.name, "applogger")
        assert_equal(currentLogLevel , 'INFO')
        assert_not_equal(currentLogLevel , 'DEBUG')

    def test_create_instance_prod(self):
        applogger = AppLogger.create_instance(__name__, self.prodconfig)
        currentLogLevel = logging.getLevelName( applogger.log.getEffectiveLevel() )
        applogger.warn("if you see this, this testcase probably failed.")
        assert_equal(applogger.log.name, __name__)
        assert_not_equal(applogger.log.name, "applogger")
        assert_equal(currentLogLevel , 'INFO')
        assert_not_equal(currentLogLevel , 'DEBUG')
        
    def test_create_instance_test(self):
        applogger = AppLogger.create_instance(__name__, self.testconfig)
        currentLogLevel = logging.getLevelName( applogger.log.getEffectiveLevel() )
        applogger.warn("if you see this, this testcase probably failed.")
        assert_equal(applogger.log.name, __name__)
        assert_not_equal(applogger.log.name, "applogger")
        assert_equal(currentLogLevel , 'DEBUG')
        assert_not_equal(currentLogLevel , 'INFO')
        
    def test_create_instance_dev(self):
        applogger = AppLogger.create_instance(__name__, self.devconfig)
        currentLogLevel = logging.getLevelName( applogger.log.getEffectiveLevel() )
        applogger.warn("if you see this, this testcase probably failed.")
        assert_equal(applogger.log.name, __name__)
        assert_not_equal(applogger.log.name, "applogger")
        assert_equal(currentLogLevel , 'DEBUG')
        assert_not_equal(currentLogLevel , 'INFO')
        
    def test_create_instance_dev_without_name(self):
        applogger = AppLogger.create_instance(appconfig=self.devconfig)
        currentLogLevel = logging.getLevelName( applogger.log.getEffectiveLevel() )
        applogger.warn("if you see this, this testcase probably failed.")
        assert_equal(applogger.log.name, __name__)
        assert_not_equal(applogger.log.name, "applogger")
        assert_equal(currentLogLevel , 'DEBUG')
        assert_not_equal(currentLogLevel , 'INFO')
        
    def test_create_instance_current(self):
        applogger = AppLogger.create_instance(__name__, self.currentconfig)
        currentLogLevel = logging.getLevelName( applogger.log.getEffectiveLevel() )
        applogger.warn("if you see this, this testcase probably failed.")
        assert_equal(applogger.log.name, __name__)
        assert_not_equal(applogger.log.name, "applogger")
        assert_equal(currentLogLevel , 'INFO')
        assert_not_equal(currentLogLevel , 'DEBUG')
    
    def test_create_instance_current_without_name(self):
        applogger = AppLogger.create_instance(appconfig=self.currentconfig)
        currentLogLevel = logging.getLevelName( applogger.log.getEffectiveLevel() )
        applogger.warn("if you see this, this testcase probably failed.")
        assert_equal(applogger.log.name, __name__)
        assert_not_equal(applogger.log.name, "applogger")
        assert_equal(currentLogLevel , 'INFO')
        assert_not_equal(currentLogLevel , 'DEBUG')
        
    
        