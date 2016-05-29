import simplejson as json

def dict_to_bytes(the_dict):
    return json.dumps(the_dict).encode()
    

