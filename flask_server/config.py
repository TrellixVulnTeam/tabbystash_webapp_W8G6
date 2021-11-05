''' Configure Flask variables separately from the application itself '''

import os
from dotenv import load_dotenv
# import sqlalchemy

# load_dotenv()


class Config():
    SESSION_TYPE = 'redis'
    SESSION_COOKIE_SECURE = True
    #GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    #GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
    GOOGLE_CLIENT_ID = '1024933268182-u8hlj1l9uiu72id99c3npuqd58u5421e.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = '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'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/anothersample'
    SECRET_KEY = 'TESTING'
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    # We don't need to make use of Flask-SQLAlchemy's event system for this app, so we turn this option off
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    DEVELOPMENT = True


# class DevConfig(Config):
#     DEBUG = True
#     DEVELOPMENT = True
