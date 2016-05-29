

try:
  basestring
except NameError:
  basestring = str



def isinstance_of_string(obj):
    return isinstance(obj, basestring)
    
    
def str_to_bytes(the_str):
    try:
      return the_str.encode()
    except AttributeError:
      return bytes(the_str)

def bytes_to_str(the_str):
    return the_str.decode()

