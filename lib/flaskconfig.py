import os
from flask import __version__ as FLASK_VERSION
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION


class FlaskConfig(object):
    DEBUG = False
    TESTING = False
    FLASK_VERSION = FLASK_VERSION
    FLASK_BOOTSTRAP_VERSION = FLASK_BOOTSTRAP_VERSION
    SECRET_KEY = SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'eoki99)u9uJ)J)J9jhgu5hg49)jjjJJKKK0Ij9jf')
    
    #DATABASE_URI = 'sqlite://:memory:'
    BOOTSTRAP_USE_MINIFIED = True
    BOOTSTRAP_USE_CDN = False
    BOOTSTRAP_FONTAWESOME = True
    

class ProductionFlaskConfig(FlaskConfig):
    pass
    #DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentFlaskConfig(FlaskConfig):
    DEBUG = True
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'secret_dev_key_24239834958495')

class TestingFlaskConfig(FlaskConfig):
    TESTING = True
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'secret_test_key_kogk94ik9gi54')