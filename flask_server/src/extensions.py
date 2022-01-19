from flask_session import Session
from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy
from argon2 import PasswordHasher
from flask_cors import CORS
#from flask_mail import Mail

#mail = Mail()

cors = CORS()

ph = PasswordHasher()

db = SQLAlchemy()

sess = Session()  # create a session object (which connects to our redis session store and stores sessions in it)

migrate = Migrate()

