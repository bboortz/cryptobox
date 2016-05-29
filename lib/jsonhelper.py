import os
from lib.pythonversionhelper import str_to_bytes
import simplejson as json

def dict_to_json(the_dict):
    return json.dumps(the_dict)
    
def json_to_dict(the_json):
    return json.loads( the_json )

def dict_to_bytes(the_dict):
    return str_to_bytes( dict_to_json(the_dict) )
    
def os_environ_to_dict():
    env = os.environ
    return dict(env)
    