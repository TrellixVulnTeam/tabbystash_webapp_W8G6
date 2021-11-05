from flask import Flask
from flask_session import Session
from config import Config
from flask_migrate import Migrate
from blueprints.authentication import authentication, oauth, login_manager
from models import db


# app = Flask(__name__)
# app.secret_key = 'TESTING'
# loads configuration variables from the same file; ie. app.py loads config variables from app.py
# app.config.from_object(DevConfig)
# Session(app)  # creates connection to redis session store


# create migrations for our database in case we update our models (ie. if we update User.py, then migrations will be created to propogate the changes into the corresponding table in the database)
# migrate = Migrate(app, db)


# configures flask-login to work with the flask application
# login_manager = LoginManager(app)

# CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
# oauth = OAuth(app)
# oauth.register(
#     name='google',
#     server_metadata_url=CONF_URL,
#     client_kwargs={
#         'scope': 'openid email profile'
#     }
# )


sess = Session()  # create a session object (which connects to our redis session store and stores sessions in it)
# create object to allow for session management and to keep track of whether or not users are already logged in

migrate = Migrate()
#bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # let sqlalchemy know about and connect to our flask application
    # db = SQLAlchemy()
    # db.create_engine(
    #     'postgresql://postgres:postgres@localhost:5432/anothersample')
    db.init_app(app)

    # db.create_all()

    sess.init_app(app)

    login_manager.init_app(app)

    migrate.init_app(app, db)

    oauth.init_app(app)

    # @app.route('/testinglogin')
    # def generic():
    #     redirect_uri = url_for('authorize', _external=True)
    #     # print('THIS IS THE URL: ', str(url_for('.oauth2_google', _external=True)))
    #     return oauth.google.authorize_redirect(redirect_uri)

    # @app.route('/authorize')
    # def authorize():
    #     token = oauth.google.authorize_access_token()
    #     userinfo = oauth.google.parse_id_token(token)
    #     if userinfo:
    #         session['userinfo'] = userinfo
    #         return redirect(url_for('loggedinpage'))
    #     return redirect(url_for('errorPage'))

    # @app.route('/errorLoggingInWithGoogle')
    # def errorPage():
    #     return '<h1> THERE WAS AN ERROR LOGGING IN WITH GOOGLE SIGN-IN </h1>'

    # @app.route('/loggedin')
    # def loggedinpage():
    #     #userInfo = session['user']
    #     # return '<h1> LOGGED IN {user}</h1>'.format(user=userInfo)
    #     return '<h1> LOGGED IN. USER INFO:{userInfo} </h1>'.format(userInfo=str(session['userinfo']))

    app.register_blueprint(authentication)

    return app


# @app.route('/')
# def hello_world():
#     keyValue = request.args.get('blah')
#     session[keyValue] = 'generic_value'
#     print('the session is:', session)
#     #print('the session id is:', session['_id'])
#     #print('the app.config stuff:', app.config)
#     return '<h1> test <h1>'


# # @app.route('/isLoggedIn')
# # def checkLoggedIn():
# #     if request.session:


# @app.route('/login')
# def login():
#     redirect_uri = url_for('auth', _external=True)
#     # print(str(oauth.google.authorize_redirect(redirect_uri)))
#     return oauth.google.authorize_redirect(redirect_uri)


# @app.route('/auth')
# def auth():
#     token = oauth.google.authorize_access_token()
#     userinfo = oauth.google.parse_id_token(token)
#     if userinfo:
#         session['userinfo'] = userinfo

#         return redirect('loggedin')
#     return redirect('errorLoggingInWithGoogleOAuth2')


# @app.route('/loggedin')
# def loggedinpage():
#     #userInfo = session['user']
#     # return '<h1> LOGGED IN {user}</h1>'.format(user=userInfo)
#     return '<h1> LOGGED IN. USER INFO:{userInfo} </h1>'.format(userInfo=str(session['userinfo']))


# @login_manager.user_loader
# def load_user(user_id):
#     return db.get(user_id)


if __name__ == '__main__':
    app = create_app()
    # dummyUser = User(3, 'admin', 'admin@gmail')
    # db.session.add(dummyUser)
    # db.session.commit()
    # print(User.query.all())
    app.run()
