from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Email

# this form is used to validate if a valid email and valid password are given in an incoming request.
# we work with the given email and password only if they pass this validator (ie. this form is just used as a preliminary check on the form data)
class EmailPasswordForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = IntegerField('password', validators=[DataRequired()])
