from src.auth import bp
from src.models import User, TabGroup, UserTabGroups
from src.auth.forms import EmailPasswordForm
from flask import request, jsonify, session, current_app
from src.extensions import ph, db#, login_manager
from flask_login import login_user, current_user
from sqlalchemy import and_
import datetime
import pytz
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import json
import smtplib
import logging

# configure our smtp connection so that we can send verification emails to users on account creation
server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)



def sendEmail(token, recipient):
    try:
        server_ssl.connect(host="smtp.gmail.com", port=465)
        server_ssl.ehlo()
        print('THIS IS THE JWT TOKEN: ', token)
        print('beginning of send mail')
        server_ssl.login(current_app.config['MAIL_USERNAME'], current_app.config['MAIL_PASSWORD'])
        emailMessage = MIMEMultipart('alternative')
        emailMessage['Subject'] = 'TabbyStash Verification'
        emailMessage['From'] = current_app.config['MAIL_USERNAME']
        emailMessage['To'] = recipient

        validationLinkForEmail = current_app.config['FRONTEND_CONFIRM_URL'] + token

        print('value of validationLink', validationLinkForEmail)

        textEmail = "This email is being sent because your email was recently registered for an account at tabbystash.com\nTo finish creating an account at tabbystash.com, verify your email by following the link: {url}".format(url=validationLinkForEmail)

        htmlEmail = """\
        <html>
        <head></head>
        <body>
            <p>This email is being sent because your email was recently registered for an account at tabbystash.com<br>
            To finish creating an account at tabbystash.com, click this <a href="{url}">link</a> to verify your email address<br>
            </p>
        </body>
        </html>
        """.format(url=validationLinkForEmail)
    

        textPartOfEmail = MIMEText(textEmail, 'plain')
        htmlPartOfEmail = MIMEText(htmlEmail, 'html')

        emailMessage.attach(textPartOfEmail)
        emailMessage.attach(htmlPartOfEmail)

        server_ssl.sendmail(current_app.config['MAIL_USERNAME'], recipient, emailMessage.as_string())

        #server_ssl.close()
        server_ssl.quit()

        print('ending of send mail')
    except BaseException as e:
        print('Failed to send verification email out to user: ', recipient)
        logging.exception('exception thrown')




    return


def deleteAllUnverifiedUsers():
    minuteAgo = datetime.datetime.utcnow() - datetime.timedelta(minutes = 1)
    unverifiedUsersToDelete = User.query.filter(User.accountUnverified==True, User.timeAccountCreated <= minuteAgo).all() # get all users whose accounts are still unverified, and whose accounts were created more than or exactly 6 hours ago
    for user in unverifiedUsersToDelete:
        db.session.delete(user)
    db.session.commit()

def loggedIn() -> bool: # return whether or not the user is logged in
    return current_user.is_authenticated


@bp.route('/verifyEmailValidationJWT', methods=['POST'])
def validate():
    print('the request.json is: ', request.json)
    userID = User.validateEmailJWT(request.json['emailToken'])
    if not userID:
        return jsonify({'error' : 'the token wasn\'t valid'})
    user = User.query.filter_by(id=userID).first()
    user.verifyUserAccount()
    db.session.add(user)
    db.session.commit()
    return jsonify({'success': 'the token was valid and the user account was verified'})


@bp.route('/resendVerificationEmail', methods=['POST'])
def resendVerifEmail():
    print('the email is: ', request.form['email'])
    user = User.query.filter_by(email=request.form['email']).first()
    print('user: ', user)
    sendEmail(user.createEmailJWT(), user.email)
    return jsonify({'success': 'email sent if account exists'})

@bp.route('/passNewAcc', methods=['POST'])
def passNewAcc():
    existingUser = User.query.filter_by(email=request.form['email']).first() # check if the email given for account registration is already in use
    if existingUser:
        return jsonify({'error': 'account already exists with specified email'})
    hashedPassword = ph.hash(request.form['password'])
    newUser = User(email=request.form['email'], password=hashedPassword)
    db.session.add(newUser)
    db.session.commit()
    sendEmail(newUser.createEmailJWT(), newUser.email)
    return jsonify({'success': 'generic data from newaccform'})

@bp.route('/passLogin', methods=['POST'])
def passLogin():
    user = User.query.filter_by(email=request.form['email']).first()
    if not user:
        return jsonify({'error': 'user account does not exist'})# if the email given by the login form doesn't correspond to an account at all in the database, then the user can't be logged in at all
    hashedPassword = user.password
    correctPasswordGiven = ph.verify(hashedPassword, request.form['password'])
    if correctPasswordGiven:
        session.permanent = True
        login_user(user)
        testUser = User.query.get(int(user.get_id()))
        print('test::', testUser)
        print('is the user logged in /passLogin? :', current_user.is_authenticated)
        return jsonify({'success': 'logged in'})
    return jsonify({'error': 'failure to login'}) # incorrect password given

@bp.route('/isLoggedIn', methods=['GET'])
def checkIfLoggedIn():
    print('everything in the session: ', session)
    print('print everything in the cookies: ', request.cookies)
    if not request.cookies:
        print('bruh')
    print('whats in the session?: ', session)
    print('the user is logged in? ', current_user.is_authenticated)
    if loggedIn():
        return jsonify({'success': 'user logged in'})
    return jsonify({'error': 'not logged in'})



@bp.route('/getTabDataFromExtension', methods=['POST'])
def getTabData():
    if loggedIn():
        tabData = request.json['tabInformation']
        print('the tab data is: ', tabData)
        tabGroup = TabGroup(tabs=tabData) # create and store the group of tabs in the database. the group of tabs needs to be committed to the database so that it gets an auto-incremented primary key automatically from the database, that can be referenced when creating a UserTabGroups row
        db.session.add(tabGroup)
        db.session.commit()

        userTabGroup = UserTabGroups(tabGroupID=tabGroup.id, userID=current_user.id)
        db.session.add(userTabGroup)
        db.session.commit()

        return jsonify({'success': 'tab data stored'})
    return jsonify({'error': 'tab data not stored'})




