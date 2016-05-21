from flask import __version__ as FLASK_VERSION
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION


class FlaskConfig(object):
    DEBUG = False
    TESTING = False
    FLASK_VERSION = FLASK_VERSION
    FLASK_BOOTSTRAP_VERSION = FLASK_BOOTSTRAP_VERSION
    
    #DATABASE_URI = 'sqlite://:memory:'
    BOOTSTRAP_USE_MINIFIED = True
    BOOTSTRAP_USE_CDN = False
    BOOTSTRAP_FONTAWESOME = True
    

class ProductionFlaskConfig(FlaskConfig):
    pass
    #DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentFlaskConfig(FlaskConfig):
    DEBUG = True

class TestingFlaskConfig(FlaskConfig):
    TESTING = True