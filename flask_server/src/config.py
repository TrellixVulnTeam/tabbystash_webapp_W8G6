""" Configure Flask variables separately from the application itself """

import os
import datetime
from dotenv import find_dotenv, load_dotenv
import redis


load_dotenv(find_dotenv())

class DevConfig:
    SESSION_TYPE = os.environ.get("SESSION_TYPE")
    SESSION_COOKIE_SECURE = os.environ.get("SESSION_COOKIE_SECURE")
    SESSION_COOKIE_NAME = os.environ.get("SESSION_COOKIE_NAME")
    SESSION_PERMANENT = False 
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=30)
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DB")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    CONF_URL = os.environ.get("CONF_URL")
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    FRONTEND_CONFIRM_URL = os.environ.get("DEV_FRONTEND_CONFIRM_URL")
    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SERVER_NAME='api.tabbystash.com'

# class ProdConfig:
#     SESSION_TYPE = os.environ.get("SESSION_TYPE")
#     SESSION_COOKIE_SECURE = os.environ.get("SESSION_COOKIE_SECURE")
#     SESSION_REDIS = redis.from_url(os.environ.get("PROD_REDIS_URL"))
#     SESSION_COOKIE_NAME = os.environ.get("SESSION_COOKIE_NAME")
#     SESSION_PERMANENT = False 
#     PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=30)
#     GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
#     GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
#     SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DB")
#     SECRET_KEY = os.environ.get("SECRET_KEY")
#     CONF_URL = os.environ.get("CONF_URL")
#     MAIL_SERVER = os.environ.get("MAIL_SERVER")
#     MAIL_PORT = os.environ.get("MAIL_PORT")
#     MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")
#     MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
#     MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
#     FRONTEND_CONFIRM_URL = os.environ.get("PROD_FRONTEND_CONFIRM_URL")
#     SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     PYTHONUNBUFFERED = True
#     SESSION_COOKIE_DOMAIN = 'tabbystash.com'
#     #SERVER_NAME='tabbystash.com:5000'
#     #SERVER_NAME = 'api.tabbystash.com'


# class TestingConfig:
#     SESSION_TYPE = os.environ.get("SESSION_TYPE")
#     SESSION_COOKIE_SECURE = os.environ.get("SESSION_COOKIE_SECURE")
#     SESSION_COOKIE_NAME = os.environ.get("SESSION_COOKIE_NAME")
#     SESSION_PERMANENT = False  
#     PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=30)
#     GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
#     GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
#     SQLALCHEMY_DATABASE_URI = os.environ.get("TESTING_DB")
#     SECRET_KEY = os.environ.get("SECRET_KEY")
#     CONF_URL = os.environ.get("CONF_URL")
#     MAIL_SERVER = os.environ.get("MAIL_SERVER")
#     MAIL_PORT = os.environ.get("MAIL_PORT")
#     MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")
#     MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
#     MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
#     FRONTEND_CONFIRM_URL = os.environ.get("FRONTEND_CONFIRM_URL")
#     SQLALCHEMY_TRACK_MODIFICATIONS = False