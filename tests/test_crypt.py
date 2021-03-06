

from lib.crypt import Crypt
from nose.tools import assert_equal
from nose.tools import assert_not_equal
#from nose.tools import assert_raises
#from nose.tools import raises


class TestCrypt(object):
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        self.crypt = Crypt()

    def teardown(self):
        """This method is run once after _each_ test method is executed"""

    def test_init(self):
        assert_equal(self.crypt.algorithm, "Fernet")
        assert_not_equal(self.crypt.algorithm, "Incorrect Value")

    def test_encrypt_and_decrypt(self):
        secret_msg = b"test message. foobar test. blub."
        token = self.crypt.encrypt(secret_msg)
        new_msg = self.crypt.decrypt(token)
        assert_equal(secret_msg, new_msg)
        assert_not_equal(secret_msg, "test message.")
        
        
#    def test_encrypt(self):
#        self.token = self.crypt.encrypt("lala")
#        print self.token
#        assert_equal(self.token, True)
#        assert_not_equal(self.token, False)
        
#    def test_decrypt(self):
#        assert_equal(self.crypt.decrypt(True, True), True)
#        assert_not_equal(self.crypt.decrypt(True, True), False)

#    def test_raise_exc(self):
#        a = A()
#        assert_raises(KeyError, a.raise_exc, "A value")

#    @raises(KeyError)
#    def test_raise_exc_with_decorator(self):
#        a = A()
#        a.raise_exc("A message")