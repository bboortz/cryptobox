
import base64
from lib.pythonversionhelper import isinstance_of_string, str_to_bytes, bytes_to_str
from lib.crypt import Crypt, PassCrypt, MultiCrypt
from cryptography.fernet import InvalidToken
from nose.tools import assert_equal
from nose.tools import assert_not_equal
#from nose.tools import assert_raises
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
        self.crypt = Crypt()
        self.passcrypt = PassCrypt()
        self.multicrypt = MultiCrypt()

    def teardown(self):
        """This method is run once after _each_ test method is executed"""

    def test_crypt_init(self):
        assert_equal(self.crypt.algorithm, "Fernet")
        assert_not_equal(self.crypt.algorithm, "Incorrect Value")

    def test_crypt_encrypt_and_check_type(self):
        secret_msg = b"test message. foobar test. blub."
        key = b"testkey"
        token = self.crypt.encrypt(secret_msg)
        assert_equal( isinstance(token, bytes), True)
        assert_not_equal( isinstance(token, bytes), False)

    def test_crypt_encrypt_and_decrypt(self):
        secret_msg = b"test message. foobar test. blub."
        key = b"testkey"
        token = self.crypt.encrypt(secret_msg)
        new_msg = self.crypt.decrypt(token)
        assert_equal(secret_msg, new_msg)
        assert_not_equal(secret_msg, "test message.")
        
    @raises(InvalidToken)
    def test_crypt_encrypt_and_decrypt_invalidtoken(self):
        secret_msg = b"test message. foobar test. blub."
        key = b"testkey"
        token = self.crypt.encrypt(secret_msg)
        token_str = bytes_to_str(token)
        token_str = "%s%s" % (token_str, 1)
        token = str_to_bytes(token_str)
        new_msg = self.crypt.decrypt(token)



    def test_passcrypt_init(self):
        assert_equal(self.passcrypt.algorithm, "Fernet")
        assert_not_equal(self.passcrypt.algorithm, "Incorrect Value")

    def test_passcrypt_encrypt_and_check_type(self):
        secret_msg = b"test message. foobar test. blub."
        password = b"testkey"
        token, key = self.passcrypt.encrypt(secret_msg, password)
        assert_equal( isinstance(token, bytes), True)
        assert_not_equal( isinstance(token, bytes), False)
        assert_equal( isinstance(key, bytes), True)
        assert_not_equal( isinstance(key, bytes), False)

    def test_passcrypt_encrypt_and_decrypt(self):
        secret_msg = b"test message. foobar test. blub."
        secret_msg_str = bytes_to_str(secret_msg)
        password = b"testkey"
        token, key = self.passcrypt.encrypt(secret_msg, password)
        new_msg = self.passcrypt.decrypt(token, key)
        assert_equal(secret_msg_str, new_msg)
        assert_not_equal(new_msg, key)
    
    def test_passcrypt_encrypt_and_decrypt_without_b(self):
        secret_msg = "test message. foobar test. blub."
        password = "testkey"
        token, key = self.passcrypt.encrypt(secret_msg, password)
        new_msg = self.passcrypt.decrypt(token, key)
        assert_equal(secret_msg, new_msg)
        assert_not_equal(new_msg, key)
    
    def test_passcrypt_encrypt_and_decrypt_base64_test(self):
        secret_msg = "test message. foobar test. blub."
        password = "testkey"
        token, key = self.passcrypt.encrypt(secret_msg, password)
        key_base64 = base64.urlsafe_b64decode(key)
        key_nobase64 = base64.urlsafe_b64encode(key_base64)
        if len(key_base64) != 32:
            raise ValueError(
                "Fernet key must be 32 url-safe base64-encoded bytes."
            )
        assert_equal(key, key_nobase64)
        assert_not_equal(key, key_base64)
        
        new_msg = self.passcrypt.decrypt(token, key_nobase64)
        assert_equal(secret_msg, new_msg)
        assert_not_equal(new_msg, key)
        
    @raises(InvalidToken)
    def test_passcrypt_encrypt_and_decrypt_invalidtoken(self):
        secret_msg = b"test message. foobar test. blub."
        password = b"testkey"
        token, key = self.passcrypt.encrypt(secret_msg, password)
        token = self.crypt.encrypt(secret_msg)
        token_str = bytes_to_str(token)
        token_str = "%s%s" % (token_str, 1)
        token = str_to_bytes(token_str)
        new_msg = self.passcrypt.decrypt(token, key)

    @raises(InvalidToken)
    def test_passcrypt_encrypt_and_decrypt_invalidtoken2(self):
        secret_msg = b"test message. foobar test. blub."
        password = b"testkey"
        token, key = self.passcrypt.encrypt(secret_msg, password)
        new_msg = self.passcrypt.decrypt(token, b'pakM9rPp1yFHrLN3K3zb0Z0oKoOc_aRYcbOTH1KO3yo=')

    def test_multicrypt_init(self):
        assert_equal(self.multicrypt.algorithm, "Fernet")
        assert_not_equal(self.multicrypt.algorithm, "Incorrect Value")

    def test_multicrypt_encrypt_and_check_type(self):
        secret_msg = b"test message. foobar test. blub."
        password = b"testkey"
        token, key1, key2 = self.multicrypt.encrypt(secret_msg, password)
        assert_equal( isinstance(token, bytes), True)
        assert_not_equal( isinstance(token, bytes), False)
        assert_equal( isinstance(key1, bytes), True)
        assert_not_equal( isinstance(key1, bytes), False)
        assert_equal( isinstance(key2, bytes), True)
        assert_not_equal( isinstance(key2, bytes), False)

    def test_multicrypt_encrypt_and_decrypt(self):
        secret_msg = b"test message. foobar test. blub."
        password = b"testkey"
        token, key1, key2 = self.multicrypt.encrypt(secret_msg, password)
        new_msg = self.multicrypt.decrypt(token, key1, key2)
        assert_equal(secret_msg, new_msg)
        assert_not_equal(new_msg, key1)
        
    def test_multicrypt_encrypt_and_decrypt_different_order(self):
        secret_msg = b"test message. foobar test. blub."
        password = b"testkey"
        token, key1, key2 = self.multicrypt.encrypt(secret_msg, password)
        new_msg = self.multicrypt.decrypt(token, key2, key1)
        assert_equal(secret_msg, new_msg)
        assert_not_equal(new_msg, key1)
        
    @raises(InvalidToken)
    def test_multicrypt_encrypt_and_decrypt_invalidtoken(self):
        secret_msg = b"test message. foobar test. blub."
        password = b"testkey"
        token, key1, key2 = self.multicrypt.encrypt(secret_msg, password)
        token = self.crypt.encrypt(secret_msg)
        token_str = bytes_to_str(token)
        token_str = "%s%s" % (token_str, 1)
        token = str_to_bytes(token_str)
        new_msg = self.multicrypt.decrypt(token, key1, key2)