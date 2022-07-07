from src.auth import bp
from src.models import User, TabGroup, UserTabGroups
from src.auth.forms import EmailPasswordForm
from flask import request, jsonify, session, current_app, make_response
from src.extensions import ph, db  # , login_manager
from flask_login import login_user, current_user, login_required
from sqlalchemy import and_
import datetime
import pytz
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import json
import smtplib
import logging

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# configure our smtp connection so that we can send verification emails to users on account creation
# server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)


# def sendEmailWithYagMail():
#     yag = yagmail.SMTP()
#     yag.send(
#         to="abedin.kadir@gmail.com",
#         subject="TabbyStash Verification",
#         contents=[
#             "This email is being sent because your email was recently registered for an account at tabbystash.com\nTo finish creating an account at tabbystash.com, click this",
#             '<p> <a href="{tabbystash.whatever}">link</a> to verify your email address </p>',
#         ],
#     )


def sendEmail(token, recipient):
    print(current_app.config)
    validationLinkForEmail = current_app.config["FRONTEND_CONFIRM_URL"] + token
    print(type("www.google.com"), "www.google.com")
    print(type(validationLinkForEmail), validationLinkForEmail)
    message = Mail(
        from_email=current_app.config["MAIL_USERNAME"],
        to_emails=recipient,
        subject="TabbyStash Verification",
        html_content = """<html>
        <head></head>
        <body>
            <p>This email is being sent because your email was recently registered for an account at tabbystash.com<br>
            To finish creating an account at tabbystash.com, click this <a href="{url}">link</a> to verify your email address<br>
            </p>
        </body>
        </html>
        """.format(url=validationLinkForEmail),
    )
    try:
        sg = SendGridAPIClient(
            current_app.config["SENDGRID_API_KEY"]
        )
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)


@bp.route("/testSendGrid")
def sendEmailWithSendGrid(token, recipient):
    sendEmail(token, recipient)
    #validationLinkForEmail = current_app.config["FRONTEND_CONFIRM_URL"] + token
    # sendEmailWithYagMail()
    return jsonify("yag done running")


# def sendEmail(token, recipient):
#     try:
#         server_ssl.connect(host="smtp.gmail.com", port=465)
#         server_ssl.ehlo()

#         server_ssl.login(
#             current_app.config["MAIL_USERNAME"], current_app.config["MAIL_PASSWORD"]
#         )
#         emailMessage = MIMEMultipart("alternative")
#         emailMessage["Subject"] = "TabbyStash Verification"
#         emailMessage["From"] = current_app.config["MAIL_USERNAME"]
#         emailMessage["To"] = recipient

#         validationLinkForEmail = current_app.config["FRONTEND_CONFIRM_URL"] + token

#         textEmail = "This email is being sent because your email was recently registered for an account at tabbystash.com\nTo finish creating an account at tabbystash.com, verify your email by following the link: {url}".format(
#             url=validationLinkForEmail
#         )

#         htmlEmail = """\
#         <html>
#         <head></head>
#         <body>
#             <p>This email is being sent because your email was recently registered for an account at tabbystash.com<br>
#             To finish creating an account at tabbystash.com, click this <a href="{url}">link</a> to verify your email address<br>
#             </p>
#         </body>
#         </html>
#         """.format(
#             url=validationLinkForEmail
#         )

#         textPartOfEmail = MIMEText(textEmail, "plain")
#         htmlPartOfEmail = MIMEText(htmlEmail, "html")

#         emailMessage.attach(textPartOfEmail)
#         emailMessage.attach(htmlPartOfEmail)

#         server_ssl.sendmail(
#             current_app.config["MAIL_USERNAME"], recipient, emailMessage.as_string()
#         )

#         # server_ssl.close()
#         server_ssl.quit()

#     except BaseException as e:

#         logging.exception("exception thrown")

#     return


def deleteAllUnverifiedUsers(elapsedMinutesToDeleteBy):
    minuteAgo = datetime.datetime.utcnow() - datetime.timedelta(
        minutes=elapsedMinutesToDeleteBy
    )
    # get all users whose accounts are still unverified, and whose accounts were created more than or exactly 6 hours ago
    unverifiedUsersToDelete = User.query.filter(
        User.accountUnverified == True, User.timeAccountCreated <= minuteAgo
    ).all()
    for user in unverifiedUsersToDelete:
        db.session.delete(user)
    db.session.commit()


def loggedIn():  # return whether or not the user is logged in, by checking if the session id (sid) is in the session
    return 'sid' in session

def deleteAllTabsForUser(user):
    allUserTabGroups = user.userTabGroups
    for userTabGroup in allUserTabGroups:
        tabGroup = TabGroup.query.filter_by(id=userTabGroup.tabGroupID).first()

        db.session.delete(userTabGroup)
        db.session.commit()

        db.session.delete(tabGroup)
        db.session.commit()


@bp.route("/deleteAllTabGroupsForUser")
def deleteAllTabGroups():
    deleteAllTabsForUser(current_user)
    return jsonify({"success": "tabs deleted"})


@bp.route("/verifyEmailValidationJWT", methods=["POST"])
def validate():
    print('beginning of validate jwt route')
    userID = User.validateEmailJWT(request.json["emailToken"])
    print('value of userID', userID)
    if not userID:
        return jsonify({"error": "the token wasn't valid"})
    user = User.query.filter_by(id=userID).first()
    user.verifyUserAccount()
    db.session.add(user)
    db.session.commit()
    return jsonify({"success": "the token was valid and the user account was verified"})


@bp.route("/resendVerificationEmail", methods=["POST"])
def resendVerifEmail():
    user = User.query.filter_by(email=request.form["email"]).first()
    sendEmail(user.createEmailJWT(), user.email)
    return jsonify({"success": "email sent if account exists"})


@bp.route("/passNewAcc", methods=["POST"])
def passNewAcc():
    # check if the email given for account registration is already in use
    existingUser = User.query.filter_by(email=request.form["email"]).first()
    if existingUser:
        return jsonify({"error": "account already exists with specified email"})
    hashedPassword = ph.hash(request.form["password"])
    newUser = User(email=request.form["email"], password=hashedPassword)
    db.session.add(newUser)
    db.session.commit()
    sendEmail(newUser.createEmailJWT(), newUser.email)
    return jsonify({"success": "generic data from newaccform"})


@bp.route("/passLogin", methods=["POST"])
def passLogin():
    user = User.query.filter_by(email=request.form["email"]).first()
    if not user:
        # if the email given by the login form doesn't correspond to an account at all in the database, then the user can't be logged in at all
        return jsonify({"error": "user account does not exist"})
    hashedPassword = user.password
    correctPasswordGiven = ph.verify(hashedPassword, request.form["password"])
    if correctPasswordGiven:
        session.permanent = True
        #print('the session should have sid now from flask-session: ', session)
        login_user(user)
        return jsonify({'success': 'logged in'})
        #resp = jsonify({'success': 'logged in'})
        #resp.set_cookie('sid', session['sid'])
        # login_user(user)
        # session['domain'] = 'tabbystash.com'
        #resp = make_response("success: logged in")
        #resp.set_cookie('sid', session['sid'])
        #print('in passLogin the session is: ', session)
        #return jsonify({"success": "logged in"})
    return jsonify({"error": "failure to login"})  # incorrect password given

@bp.after_request
def checkResponse(response):
    #print('the users html response headers are: ', response.headers.getlist('Set-Cookie'))
    print('testing')
    print('the response from after request is: ', response)
    print('the headers: ', response.headers)
    return response

@bp.route('/testCookie', methods=['POST'])
def checkCookie():
    resp = make_response()
    # resp.headers['Set-Cookie'] = 'bruh=hello'
    resp.set_cookie('hi', 'there', domain='tabbystash.com')
    return resp

@bp.route('/testIfFlaskGetsCookie', methods=['GET'])
def checkIfFlaskGetsCookie():
    print('the request in flaskgetscookie is: ', request)
    print('the headers are: ', request.headers)
    print('the cookies are: ', request.cookies)
    # print('the session\'s domain header: ', )
    return jsonify({'generic': 'response'})

@bp.route("/isLoggedIn", methods=["GET"])
def checkIfLoggedIn():
    if current_user.is_authenticated:
        return jsonify({"success": "user logged in"})
    return jsonify({"error": "not logged in"})

@bp.route('/loginTestUser')
def loginTestUser():
    user = User.query.filter_by(email='abedin.kadir@gmail.com').first()
    login_user(user)
    return jsonify({'example': 'login response'})

@bp.route('/checkRequest')
def checkRequest():
    print('the request is: ', request.headers)
    return jsonify({'request': str(request.headers)})

# @bp.after_request
# def changeDomainOnCookie(response):
#     print('the response that would be sent out is: ', response.headers['Set-Cookie'])
#     return response


@bp.route("/storeTabDataFromExtension", methods=["POST"])
def storeTabData():
    if current_user.is_authenticated:
        tabGroup = TabGroup(
            tabs=request.json["tabData"], nameOfTabGroup=request.json["tabGroupName"]
        )  # create and store the group of tabs in the database. the group of tabs needs to be committed to the database so that it gets an auto-incremented primary key automatically from the database, that can be referenced when creating a UserTabGroups row
        db.session.add(tabGroup)
        db.session.commit()

        userTabGroup = UserTabGroups(tabGroupID=tabGroup.id, userID=current_user.id)
        db.session.add(userTabGroup)
        db.session.commit()
        return jsonify({"success": "tab data stored"})
    return jsonify({"error": "not logged in"})


@bp.route("/getUserTabData", methods=["GET"])
def getUserTabData():
    if current_user.is_authenticated:
        allOfUsersTabGroups = current_user.userTabGroups
        tabGroups = []
        for userTabGroup in allOfUsersTabGroups:
            tabGroup = TabGroup.query.filter_by(id=userTabGroup.tabGroupID).first()
            # tabGroupData = {str(tabGroup.nameOfTabGroup): tabGroup.tabs}
            tabGroups.append(
                {
                    "tabGroupName": tabGroup.nameOfTabGroup,
                    "tabGroupData": {
                        "tabs": tabGroup.tabs,
                        "timestampTabGroupSaved": str(
                            tabGroup.timeTabGroupCreated
                        ),  # convert the UTC timestamp for the TabGroup into a string, so that it doesn't get converted into a GMT timestamp by the axios call from the Next.js frontend
                    },
                }
            )
            print("the timestamp for this tab group: ", tabGroup.timeTabGroupCreated)
        if not tabGroups:
            # we need to be able to tell the difference between if no data is returned from this view because the user just doesn't have any, or because there was an error with them not being logged in
            return jsonify({"success": []}) # no data for the user
        return jsonify({"success": tabGroups})
    # if the user isn't logged in, then you can't return tab data for the frontend to render
    return jsonify({"error": "can't load tab data for user"})


# @bp.route("/config", methods=["GET"])
# def checkEnvVariables():
#     print("the current config is: ", current_app.config)
#     return jsonify(current_app.config)


@bp.route("/html", methods=["GET"])
def returnGenericHtml():
    return "<h1> Hello! </h1>"
