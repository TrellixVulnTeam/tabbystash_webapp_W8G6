from flask import Blueprint
from flask import session, make_response, request
from src.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')



# def _build_cors_preflight_response():
#     resp = make_response()
#     resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
#     resp.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
#     resp.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
#     resp.headers['Access-Control-Allow-Credentials'] = 'true'
#     session.clear()    
#     return resp

# def _corsify_actual_response(response):
#     response.headers.add("Access-Control-Allow-Origin",
#                          "http://localhost:3000")
#     response.headers.add('Access-Control-Allow-Credentials', 'true')
#     return response

# @bp.after_request
# def corsResponse(response):
#     if request.method == 'OPTIONS': # if the request is an OPTIONS request, then return a response with the proper CORS headers and delete the session ID that gets automatically created by Flask-Login, so that we don't store an extra session in Redis
#         return _build_cors_preflight_response()
#     print('im in after request, my request method is: ', request.method)
#     return _corsify_actual_response(response)

# @login_manager.user_loader
# def load_user(userID):
#     return User.query.filter_by(id=userID).first()

from src.auth import google
from src.auth import emailpassword