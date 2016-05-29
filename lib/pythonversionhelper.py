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
      #return bytes(str, 'utf-8')
      return str.encode()
    except TypeError:
      #return bytes(str)
      return str.encode('utf-8')
    except AttributeError:
      return bytes(str)

def bytes_to_str(str):
    try:
      #return bytes(str, 'utf-8')
      return str.decode()
    except TypeError:
      #return bytes(str)
      return str.decode('utf-8')
