from flask import request

def is_mimetype_json():
    if request.headers['Content-Type'] == 'application/json':
        return True
        
    return False

def request_wants_json():
    best = request.accept_mimetypes.best_match(['application/json', 'text/html'])
    return best == 'application/json' and request.accept_mimetypes[best] > request.accept_mimetypes['text/html']