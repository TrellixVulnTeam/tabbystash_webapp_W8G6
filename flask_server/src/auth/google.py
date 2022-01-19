from flask import Blueprint, session, request, jsonify, redirect, url_for
from flask.helpers import make_response
from flask_login.utils import login_required
# from authlib.integrations.flask_client import OAuth
#from src import db
#import src
from src.auth import bp
#from src.models import User
#from flask_cors import cross_origin
from flask_login import current_user, login_user, LoginManager
#from blueprints.forms import EmailPasswordLoginForm
import requests
import json

#import src.authroutes
#from src.authroutes import bp



# def _build_cors_preflight_response():
#     response = make_response()
#     response.headers.add("Access-Control-Allow-Origin",
#                          'http://localhost:3000')
#     response.headers.add('Access-Control-Allow-Headers',
#                          'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods',
#                          'GET,PUT,POST,DELETE,OPTIONS')
#     response.headers.add('Access-Control-Allow-Credentials', 'true')
#     session.clear()
#     return response


# def _corsify_actual_response(response):
#     response.headers.add("Access-Control-Allow-Origin",
#                          "http://localhost:3000")
#     response.headers.add('Access-Control-Allow-Credentials', 'true')
#     return response

# login_manager = LoginManager()


# @login_manager.user_loader
# def load_user(id):
#     return User.query.get(int(id))


# def responseAfterAuthentication():
#     if not current_user.is_authenticated:
#         print('not authenticated 3')
#     if current_user.is_authenticated:
#         return {'success': {
#             'message': 'authentication was successful'
#         }}
#     else:
#         return {'failure': {
#             'message': 'authentication failed'
#         }}

# this ^ block of code is meant to work with Flask Login, to tell if a user is authenticated.
# In Flask Login we would authenticate/login users by doing login(a User object)

# @bp.route('/googleLogin', methods=['GET', 'OPTIONS'])
# def googleLogin():
#     if request.method == 'OPTIONS':
#         return _build_cors_preflight_response()
#     elif request.method == 'GET':
#         authCode = request.headers['Authorization']
#         paramsForGoogleAccessCode = {'code': authCode, 'client_id': '1024933268182-u8hlj1l9uiu72id99c3npuqd58u5421e.apps.googleusercontent.com', 'client_secret':'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', 'grant_type':'authorization_code', 'redirect_uri':'postmessage'}
#         data = (requests.post('https://oauth2.googleapis.com/token', data=paramsForGoogleAccessCode)).json()

#         urlToSendToGoogle = 'https://www.googleapis.com/oauth2/v1/userinfo?access_token=' + \
#         data['access_token']
#         respFromGoogleJSONString = requests.get(urlToSendToGoogle).content
#         respFromGoogleDict = json.loads(respFromGoogleJSONString)
#         return _corsify_actual_response(jsonify({'data': 'generic data'}))
#     else:
#         raise RuntimeError(
#             '#todo: put error message to describe what happens if http request isnt get or options')

@bp.route('/testGoogleCallback')
def callback():
    if request.method == 'OPTIONS':
        return
    print('callback worked')
    return jsonify({'data': 'callback data'})


@bp.route('/dummy', methods=['GET', 'OPTIONS'])
def dummy():
    if request.method == 'OPTIONS':
        # todo: options requests can now be manually dealt with. so now you need to delete the session cookie for the options request that comes with the CORS request, so that the Redis database doesnt store 2 sessions with 1 CORS request
        print('AAAAAAAAAAA GO CRAZY AAAAAAAAAAAA GO STUPID ', request.method)
        return _build_cors_preflight_response()
    elif request.method == 'GET':
        # return jsonify({'data': 'generic data'})
        return _corsify_actual_response(jsonify({'data': 'generic data'}))
    else:
        raise RuntimeError(
            '#todo: put error message to describe what happens if http request isnt get or options')

    # if request.method == "OPTIONS":
    #     print('options method accessed')

    #     response = make_response(jsonify({'data': 'generic data'}))
    #     response.headers.add("Access-Control-Allow-Origin",
    #                          "http://localhost:3000")
    #     response.headers.add("Access-Control-Allow-Methods", "*")
    #     response.headers.add("Access-Control-Allow-Headers", "*")
    #     print('this is the response to return for options', response.headers)
    #     return response

    # elif request.method == "GET":
    #     response = make_response(jsonify({'get': 'some data idk'}))
    #     response.headers.add("Access-Control-Allow-Origin",
    #                          "http://localhost:3000")
    #     return response

    # else:
    #     print('what?')

    # print('request coming!', request.method)
    # print('my session is: ', list(session.keys()))
    # if request.method == 'GET':
    #     session['bruh'] = 'anotherbruh'
    # return jsonify({'data': 'generic data'})


@bp.route('/cookie')
def listCookie():
    if request.cookies:
        session['BLABLABLA'] = 'BACCHAE'
        return 'the cookie exists: {cookieInfo}'.format(cookieInfo=request.cookies)
    return 'the cookie doesn\'t exist'


# @bp.route('/email_password_login')
# def emailPassLogin():
#     # TODO: I need to validate the password given in the login form; use the argon2 library in flask to hash the passwords, and decrypt the hash here to see if the passwords are the same
#     loginForm = EmailPasswordLoginForm()
#     if loginForm.validate_on_submit():
#         existingUser = User.query.filter_by(email=loginForm.email).first()
#         if existingUser:  # if a user tries to login by email and password, and their email given exists in our database, then we don't need to create a new User profile, and we can use their existing information
#             return '<h1> the login credentials you gave correspond to a user in the databsae </h1>'
#         newUser = User(email='BLABLABLABLA@gmail.com', password=12312323)
#         db.session.add(newUser)
#         db.session.commit()
#         login_user(newUser)


# @bp.route('/login')
# @cross_origin(supports_credentials=True)
# def loginHandler():
#     print('the session is NOW : ', session)
#     if not current_user.is_authenticated:
#         print('not authenticated 3')
#     if current_user.is_authenticated:
#         return {'success': {
#             'message': 'authentication was successful'
#         }}
#     else:
#         return {'failure': {
#             'message': 'authentication failed'
#         }}
    # tell whether or not the person is logging in with google oauth or with regular email/password


@bp.route('/testCookies')
# @cross_origin(supports_credentials=True)
def testCookies():
    # return jsonify({'data': 'data inside testCookies'})
    return redirect(url_for('.loginHandler'))


@bp.route('/google_oauth2_login')
#@cross_origin(supports_credentials=True)
def redirectToGoogleOAuth():
    if request.method == 'OPTIONS':
        print('HIIIIIIIIIIIIIII')
    print('this is the id token sent over: ', request.headers['Authorization'])
    urlToSendToGoogle = 'https://oauth2.googleapis.com/tokeninfo?id_token=' + \
        request.headers['Authorization']
    respFromGoogleJSONString = requests.get(urlToSendToGoogle).content
    respFromGoogleDict = json.loads(respFromGoogleJSONString)
    if 'error' in respFromGoogleDict:
        print('ran into an error, because the user closed the popup')
    print('what the url should look like', urlToSendToGoogle)
    respFromGoogleJSONString = requests.get(urlToSendToGoogle).content
    print('IS THIS EMPTY?: ', respFromGoogleJSONString)
    if not respFromGoogleJSONString:
        return redirect(url_for('.loginHandler'))
    user = src.models.User.query.filter_by(email=respFromGoogleDict['email']).first()
    if not user:  # if there isn't a user that already exists with this email, we need to create a new User, and store it in the database, and then create a session for them
        user = src.models.User(email=respFromGoogleDict['email'])
        src.db.session.add(user)
        src.db.session.commit()
    if current_user.is_authenticated:
        print('authenticated 1')
    print('users id:', user.id)
    login_user(user)
    if current_user.is_authenticated:
        print('authenticated 2')
    print('the session is: ', session)
    print('THE COOKIE IS: ', request.cookies)
    # return responseAfterAuthentication()
    # at this point, the user has already been made if it hasn't been made before, and we know a valid, non-empty response came in from Google, so we can login the user and return a response to our frontend
    return redirect(url_for('.loginHandler'))


@bp.route('/google_oauth2_authorize')
# @cross_origin()
def googleAuthorize():
    # print("a request is coming from: ", request.remote_addr)
    # token = oauth.google.authorize_access_token()
    # user = token.get('userinfo')
    # print('this is all the information i have about the user:', user)
    # print(request.headers['Authorization'])
    # googleAuthToken = request.headers['Authorization']
    # r = requests.get(
    #     'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token={token}'.format(token=googleAuthToken))
    # print('this is what r produced?', r.json())
    return jsonify({'data': 'generic data from oauth2 authorize'})

    # return jsonify({'data': '{token}'.format(token=googleAuthToken)})
    # print('testing if this route is hit')
    # return 'response from flask server'

    # token = oauth.google.authorize_access_token()
    # userinfo = oauth.google.parse_id_token(token)
    # print('this is the userinfo', userinfo)
    # # query the database to see if the email returned by the google oauth2 access token exists in our database. if it does, we have an existing user, so we can directly log them in
    # user = User.query.filter_by(email=userinfo['email']).first()
    # if user:
    #     login_user(user)
    #     # because the user is now logged in, we redirect them to the loginHandler view so that a JSON response can be sent back to the frontend, to indicate that the authentication was successful
    #     return redirect(url_for('.loginHandler'))
    # # if the user doesn't exist, then we need to create a new user in our database
    # user = User(email=userinfo['email'])
    # db.session.add(user)
    # db.session.commit()
    # login_user(user)
    # return redirect(url_for('.loginHandler'))


@bp.route('/errorLoggingInWithGoogle')
def errorPage():
    return '<h1> THERE WAS AN ERROR LOGGING IN WITH GOOGLE SIGN-IN </h1>'


@bp.route('/loggedin')
def loggedInPage():
    #userInfo = session['user']
    # return '<h1> LOGGED IN {user}</h1>'.format(user=userInfo)
    return '<h1> LOGGED IN. USER INFO:{userInfo} </h1>'.format(userInfo=str(session['userinfo']))
    # return '<h1> you are logged in! </h1>'
