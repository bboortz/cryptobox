import os
import platform

from lib.flaskconfig import ProductionFlaskConfig, DevelopmentFlaskConfig, TestingFlaskConfig

class AppConfig(object):
    APPNAME = "test"
    APPVERSION = "0.1"
    ENV = "PROD"
    IP = os.getenv('IP', '0.0.0.0')
    PORT = int( os.getenv('PORT', 8080) )
    PYTHONVERSION = platform.python_version()
    FLASKCONFIG = ProductionFlaskConfig
    
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
            'flask-version': self.FLASKCONFIG.__version__ ,
            'flask-debug': self.FLASKCONFIG.DEBUG ,
            'flask-testing': self.FLASKCONFIG.TESTING ,
        } 
        
        return result
    
    def api_to_json(self):
        result = { 
            'api': self.APPNAME, 
            'api-version': self.APPVERSION, 
            'python-version': self.PYTHONVERSION,
            'flask-version': self.FLASKCONFIG.__version__ 
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