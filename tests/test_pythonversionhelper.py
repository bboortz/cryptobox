

from lib.pythonversionhelper import *
from nose.tools import assert_equal
from nose.tools import assert_not_equal



class TestPythonVersionHelper(object):
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        pass

    def teardown(self):
        """This method is run once after _each_ test method is executed"""

    def test_isinstance_of_string(self):
        assert_equal( isinstance_of_string("  "), True)
        assert_equal( isinstance_of_string("123131"), True)
        assert_equal( isinstance_of_string(u"  "), True)
        assert_equal( isinstance_of_string(u"aasds"), True)
        assert_equal( isinstance_of_string(b"  "), True)
        assert_equal( isinstance_of_string(b"asdasdsa"), True)
        
        assert_not_equal( isinstance_of_string(123434), True)
        