import simplejson as json

def dict_to_bytes(the_dict):
    return json.dumps(the_dict).encode()
    
def str_to_bytes(str):
    return str.encode()
