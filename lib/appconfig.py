import os

from lib.flaskconfig import ProductionFlaskConfig, DevelopmentFlaskConfig, TestingFlaskConfig

class AppConfig(object):
    IP = os.getenv('IP', '0.0.0.0')
    PORT = int( os.getenv('PORT', 8080) )
    APPNAME = "test"
    APPVERSION = "0.1"
    ENV = "PROD"
    FLASKCONFIG = ProductionFlaskConfig
    
    @staticmethod
    def create_instance( env=os.getenv('ENV', 'PROD') ):
        result = ProductionAppConfig()
        
        if env == 'DEV':
            result = DevelopmentAppConfig()
        elif env == 'TEST':
            result = TestingAppConfig()
            
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