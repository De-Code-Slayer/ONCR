from app.user.controllers.users_controllers import  check_token
from app import abort, request
from functools import wraps
import json


def logged_in( function ):
    @wraps( function )
    def wrapper_function( *args, **kwargs ):
        token = check_token(request.cookies.get('refresh_token'))
        if 'code' in token and 'exceptionThrown' in token:
            return abort(401, description={"error": "User is Unathorized to view this resource",  "message": f'{token}', "code": 401 })
        else:
            return function( *args, **kwargs )
       
    return wrapper_function