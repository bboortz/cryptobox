from cryptography.fernet import Fernet


class Crypt:

    def __init__(self):
        self.algorithm = "Fernet"
        key = Fernet.generate_key()
        self.f = Fernet(key)
    
    def encrypt(self, data):
        return self.f.encrypt(data)
        
    def decrypt(self, token):
        return self.f.decrypt(token)
        
    