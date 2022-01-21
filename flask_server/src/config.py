''' Configure Flask variables separately from the application itself '''

import os
import datetime
# from dotenv import load_dotenv
# import sqlalchemy

# load_dotenv()


class Config:
    SESSION_TYPE = os.environ.get('SESSION_TYPE')
    #SESSION_TYPE = os.environ.get('SESSION_TYPE')
    SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE')
    #SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE')
    SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME')
    SESSION_PERMANENT = False#os.environ.get('SESSION_PERMANENT')
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=30)
    #SESSION_COOKIE_HTTPONLY = False
    #GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    #GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    CONF_URL = os.environ.get('CONF_URL')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FRONTEND_CONFIRM_URL = os.environ.get('FRONTEND_CONFIRM_URL')
    # We don't need to make use of Flask-SQLAlchemy's event system for this app, so we turn this option off
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    # CORS_ORIGINS = 'http://localhost:3000'


# class DevConfig(Config):
#     DEBUG = True
#     DEVELOPMENT = True
