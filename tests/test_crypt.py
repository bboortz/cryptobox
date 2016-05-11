import os
import sys
testdir = os.path.dirname(__file__)
srcdir = '..'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from lib.crypt import Crypt
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises


class TestCrypt(object):
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

    def test_init(self):
        crypt = Crypt()
        assert_equal(crypt.algorithm, "AES")
        assert_not_equal(crypt.algorithm, "Incorrect Value")

    def test_encrypt(self):
        crypt = Crypt()
        assert_equal(crypt.encrypt(True, True), True)
        assert_not_equal(crypt.encrypt(True, True), False)
        
    def test_decrypt(self):
        crypt = Crypt()
        assert_equal(crypt.decrypt(True, True), True)
        assert_not_equal(crypt.decrypt(True, True), False)

#    def test_raise_exc(self):
#        a = A()
#        assert_raises(KeyError, a.raise_exc, "A value")

#    @raises(KeyError)
#    def test_raise_exc_with_decorator(self):
#        a = A()
#        a.raise_exc("A message")