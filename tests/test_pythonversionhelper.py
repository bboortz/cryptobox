

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
    
    def test_str_to_bytes(self):
        str = "this is a test string"
        ustr = u"this is a test string type unicode"
        bstr = b"this is a test string type byte"
        
        assert_equal( isinstance_of_string( str ), True)
        assert_equal( isinstance_of_string( ustr ), True)
        assert_equal( isinstance_of_string( bstr ), True)
        
        str_byte = str_to_bytes(str)
        ustr_byte = str_to_bytes(ustr)
        bstr_byte = str_to_bytes(bstr)
        
        print type (str_byte)
        print type (ustr_byte)
        print type (bstr_byte)
        print type ( str_to_bytes("  ") )
        print str.encode()
        assert_equal( isinstance_of_string("  "), False)
        assert_equal( isinstance_of_string("123131"), True)
        assert_equal( isinstance_of_string(u"  "), True)
        assert_equal( isinstance_of_string(u"aasds"), True)
        assert_equal( isinstance_of_string(b"  "), True)
        assert_equal( isinstance_of_string(b"asdasdsa"), True)
        
        assert_not_equal( isinstance_of_string(123434), True)
        