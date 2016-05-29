from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper

try:
  basestring
except NameError:
  basestring = str



def isinstance_of_string(obj):
    return isinstance(obj, basestring)
    
    
def str_to_bytes(str):
    try:
      return str.encode()
    except AttributeError:
      return bytes(str)

def bytes_to_str(str):
    return str.decode()

