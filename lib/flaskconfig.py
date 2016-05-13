from flask import jsonify, __version__


class FlaskConfig(object):
    DEBUG = False
    TESTING = False
    __version__ = __version__
    #DATABASE_URI = 'sqlite://:memory:'
    

class ProductionFlaskConfig(FlaskConfig):
    pass
    #DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentFlaskConfig(FlaskConfig):
    DEBUG = True

class TestingFlaskConfig(FlaskConfig):
    TESTING = True