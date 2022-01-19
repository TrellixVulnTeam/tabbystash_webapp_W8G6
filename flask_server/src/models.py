from flask_login import UserMixin
from src.extensions import db
import datetime
import pytz
from sqlalchemy.sql import expression
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.types import DateTime
import jwt
from flask import current_app

class utcnow(expression.FunctionElement):
    type = DateTime()
    inherit_cache = True

@compiles(utcnow, 'postgresql')
def pg_utcnow(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    #server_default=utcnow()
    #timeAccountCreated = db.Column(db.DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    timeAccountCreated = db.Column(db.DateTime, nullable=False, server_default=utcnow())#default=datetime.now(tz=timezone('US/Eastern')))#default=utcnow)#default=datetime.strftime(datetime.now(tz=timezone('US/Eastern')), "%Y-%m-%d %H:%M:%S"))
    accountUnverified = db.Column(db.Boolean, nullable=False, default=True)

    def createEmailJWT(self, expires_in=1800):
        return jwt.encode(
            {'emailValidate': self.id, 'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds = expires_in)},
            current_app.config['SECRET_KEY'],
            algorithm="HS256"
        )

    @staticmethod
    def validateEmailJWT(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
            algorithms='HS256')['emailValidate']
            print('id is: ', id)
            return id
        except:
            #return False #need to add error message here, and handle the case in which a JWT is not valid
            return None
        #return True

    def verifyUserAccount(self):
        self.accountUnverified = False
        

    

    