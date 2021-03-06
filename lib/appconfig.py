import os
import platform

from lib.flaskconfig import ProductionFlaskConfig, DevelopmentFlaskConfig, TestingFlaskConfig

class AppConfig(object):
    APPNAME = "cryptobox"
    APPVERSION = "0.1.6"
    ENV = "PROD"
    IP = os.getenv('IP', '0.0.0.0')
    PORT = int( os.getenv('PORT', 8080) )
    PYTHONVERSION = platform.python_version()
    FLASKCONFIG = ProductionFlaskConfig
    
    
    API_URL = "https://localhost:8081"
    if 'DYNO' in os.environ:
        API_PORT = os.getenv('API_PORT', 443)
        API_URL = os.getenv('API_URL', "https://cryptobox.herokuapp.com:%s" % API_PORT)
    elif 'C9_HOSTNAME' in os.environ:
        HOSTNAME = os.getenv('C9_HOSTNAME', 'cryptobox-bboortz.c9users.io')
        API_PORT = os.getenv('API_PORT', 8080)
        API_URL = os.getenv('API_URL', "https://%s:%s" % (HOSTNAME, API_PORT) )
    
    
    
    @staticmethod
    def create_instance( env=os.getenv('ENV', 'PROD') ):
        result = ProductionAppConfig()
        
        if env == 'DEV':
            result = DevelopmentAppConfig()
        elif env == 'TEST':
            result = TestingAppConfig()
            
        return result
        
    def config_to_json(self):
        result = { 
            'api': self.APPNAME, 
            'api-version': self.APPVERSION, 
            'ENV': self.ENV,
            'IP': self.IP,
            'PORT': self.PORT,
            'python-version': self.PYTHONVERSION,
            'flask-version': self.FLASKCONFIG.FLASK_VERSION ,
            'flask-debug': self.FLASKCONFIG.DEBUG ,
            'flask-testing': self.FLASKCONFIG.TESTING ,
            'flask-bootstrap-version': self.FLASKCONFIG.FLASK_BOOTSTRAP_VERSION,
        } 
        
        return result
    
    def api_to_json(self):
        result = { 
            'api': self.APPNAME, 
            'api-version': self.APPVERSION, 
            'python-version': self.PYTHONVERSION,
            'flask-version': self.FLASKCONFIG.FLASK_VERSION,
            'flask-bootstrap-version': self.FLASKCONFIG.FLASK_BOOTSTRAP_VERSION,
        } 
        return result

class ProductionAppConfig(AppConfig):
    ENV = "PROD"
    FLASKCONFIG = ProductionFlaskConfig

class DevelopmentAppConfig(AppConfig):
    ENV = "DEV"
    FLASKCONFIG = DevelopmentFlaskConfig

class TestingAppConfig(AppConfig):
    ENV = "TEST"
    FLASKCONFIG = TestingFlaskConfig