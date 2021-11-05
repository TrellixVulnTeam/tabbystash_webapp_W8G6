from flask import Blueprint, url_for, session, redirect, request
from authlib.integrations.flask_client import OAuth
from models import db, User
from flask_login import current_user, login_user, LoginManager
#from flask_login import LoginManager
#from forms import EmailPasswordLoginForm
#import forms
#from forms import testaasdasd
from blueprints.forms import EmailPasswordLoginForm

login_manager = LoginManager()

oauth = OAuth()  # create oauth object to make connections to google's oauth2 endpoint
oauth.register(
    'google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)

authentication = Blueprint('authentication', __name__,
                           url_prefix='/authentication')


@login_manager.user_loader
def get_user(ident):
    return User.query.get(int(ident))


# @login_manager.unauthorized_handler
# def unauthorized_request():  # if a user tries to go past the login page in our frontend to the core webapp directly, then they need to be redirected to the login page, which is what this callback function does
#     return redirect(url_for('.loginHandler'))


@authentication.route('/asd')
def asd():
    return '<h1> bruh </h1>'


@authentication.route('/cookie')
def listCookie():
    if request.cookies:
        session['BLABLABLA'] = 'BACCHAE'
        return 'the cookie exists: {cookieInfo}'.format(cookieInfo=request.cookies)
    return 'the cookie doesn\'t exist'


@authentication.route('/email_password_login')
def emailPassLogin():
    # TODO: I need to validate the password given in the login form; use the argon2 library in flask to hash the passwords, and decrypt the hash here to see if the passwords are the same
    loginForm = EmailPasswordLoginForm()
    if loginForm.validate_on_submit():
        existingUser = User.query.filter_by(email=loginForm.email)
        if existingUser:  # if a user tries to login by email and password, and their email given exists in our database, then we don't need to create a new User profile, and we can use their existing information
            return '<h1> the login credentials you gave correspond to a user in the databsae </h1>'
        newUser = User(email='BLABLABLABLA@gmail.com', password=12312323)
        db.session.add(newUser)
        db.session.commit()
        login_user(newUser)


@authentication.route('/login')
def loginHandler():
    if current_user.is_authenticated:
        return {'success': {
            'message': 'authentication was successful'
        }}
    else:
        return {'failure': {
            'message': 'authentication failed'
        }}
        # tell whether or not the person is logging in with google oauth or with regular email/password


@authentication.route('/google_oauth2_login')
def redirectToGoogleOAuth():
    redirect_uri = url_for('.googleAuthorize', _external=True)
    # print('THIS IS THE URL: ', str(url_for('.oauth2_google', _external=True)))
    return oauth.google.authorize_redirect(redirect_uri)
    # variable = str(url_for('.oauth2_google', _external=True))
    # return f'<h1> the url to go to is: {variable}'


# @authentication.route('/dummyUser')
# def dummyUserAdd():
#     dummyUser = User(userId=1, name='abedin', email='generic@gmail')
#     db.session.add(dummyUser)
#     db.session.commit()


@authentication.route('/dummyRoute')
def dummyUserRoute():
    print('AM I LOGGED IN AT DUMMY ROUTE: ', current_user.is_authenticated)
    return '<h1> something generic </h1>'


@authentication.route('/google_oauth2_authorize')
def googleAuthorize():
    token = oauth.google.authorize_access_token()
    userinfo = oauth.google.parse_id_token(token)
    # query the database to see if the email returned by the google oauth2 access token exists in our database. if it does, we have an existing user, so we can directly log them in
    user = User.query.filter_by(userinfo['email'])
    if user:
        login_user(user)
        # because the user is now logged in, we redirect them to the loginHandler view so that a JSON response can be sent back to the frontend, to indicate that the authentication was successful
        return redirect(url_for('.loginHandler'))
    # if the user doesn't exist, then we need to create a new user in our database
    user = User(email=userinfo['email'], googleID=userinfo['sub'])
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return redirect(url_for('.loggedInPage'))


@authentication.route('/errorLoggingInWithGoogle')
def errorPage():
    return '<h1> THERE WAS AN ERROR LOGGING IN WITH GOOGLE SIGN-IN </h1>'


@authentication.route('/loggedin')
def loggedInPage():
    #userInfo = session['user']
    # return '<h1> LOGGED IN {user}</h1>'.format(user=userInfo)
    return '<h1> LOGGED IN. USER INFO:{userInfo} </h1>'.format(userInfo=str(session['userinfo']))
    # return '<h1> you are logged in! </h1>'
