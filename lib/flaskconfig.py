import os

class FlaskConfig(object):
    DEBUG = False
    TESTING = False
    #DATABASE_URI = 'sqlite://:memory:'

class ProductionFlaskConfig(FlaskConfig):
    pass
    #DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentFlaskConfig(FlaskConfig):
    DEBUG = True

class TestingFlaskConfig(FlaskConfig):
    TESTING = True