from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper

try:
  basestring
except NameError:
  basestring = str



def isinstance_of_string(obj):
    return isinstance(obj, basestring)
