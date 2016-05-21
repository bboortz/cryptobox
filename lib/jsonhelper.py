import simplejson as json

def dict_to_bytes(the_dict):
    str = json.dumps(the_dict)
    return str.encode()
    
def string_to_dict(str):
    return json.loads(str)