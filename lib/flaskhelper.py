from lib.pythonversionhelper import isinstance_of_string
from datetime import timedelta
from flask import make_response, request, current_app, abort
from functools import update_wrapper



def is_mimetype_json():
    if request.headers['Content-Type'] == 'application/json':
        return True
        
    return False
    
    
def abort_on_zero_string(the_str):
    if not isinstance_of_string(the_str):
        abort(400)
    if the_str == None  or  the_str == ""  or  the_str.__sizeof__() == 0:
        abort(400)
    
    


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance_of_string(headers):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance_of_string(origin):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

#def request_wants_json():
#    best = request.accept_mimetypes.best_match(['application/json', 'text/html'])
#    return best == 'application/json' and request.accept_mimetypes[best] > request.accept_mimetypes['text/html']