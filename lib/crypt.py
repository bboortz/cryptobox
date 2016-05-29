import os
import base64
from lib.pythonversionhelper import isinstance_of_string, str_to_bytes, bytes_to_str
from cryptography.fernet import Fernet, MultiFernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Crypt:

    def __init__(self):
        self.algorithm = "Fernet"
        key = Fernet.generate_key()
        self.f = Fernet(key)
    
    def encrypt(self, data):
        return self.f.encrypt(data)
        
    def decrypt(self, token):
        return self.f.decrypt(token)
        
class PassCrypt:

    def __init__(self):
        self.algorithm = "Fernet"
    
    @classmethod
    def convertPassToKey(cls, password):
        if isinstance_of_string(password):
            password = str_to_bytes(password)
        
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key
    
    def encrypt(self, data, password):
        if isinstance_of_string(data):
            data = str_to_bytes(data)
            
        key =  PassCrypt.convertPassToKey(password)
        f = Fernet(key)
        return (f.encrypt(data), key)
        
    def decrypt(self, token, key):
        f = Fernet(key)
        msg = f.decrypt(token)
        return bytes_to_str(msg)


class MultiCrypt:

    def __init__(self):
        self.algorithm = "Fernet"
    
    def encrypt(self, data, password):
        key1 = Fernet.generate_key()
        key2 = PassCrypt.convertPassToKey(password)
        fernet_key1 = Fernet(key1)
        fernet_key2 = Fernet(key2)
        f = MultiFernet([fernet_key1, fernet_key2])
        token = f.encrypt(data)
        return token, key1, key2
        
    def decrypt(self, token, key1, key2):
        fernet_key1 = Fernet(key1)
        fernet_key2 = Fernet(key2)
        f = MultiFernet([fernet_key1, fernet_key2])
        return f.decrypt(token)
