import pytest
import os

from src import create_app
from src.extensions import db
from src.models import User
from flask import current_app

# from src.configTest import TestingConfig

# TODO: Database is not being created properly in tests -> fix


@pytest.fixture
def testingApp():
    return create_app()


# def setup_function():
#     print("setting up")


# def test_myoutput(capsys):  # or use "capfd" for fd-level
#     print("hello")
#     with capsys.disabled():
#         print("testing not captured")
# sys.stderr.write("world\n")
# captured = capsys.readouterr()
# assert captured.out == "helo\n"
# assert captured.err == "world\n"
# print("next")
# captured = capsys.readouterr()
# assert captured.out == "next\n"
# assert False
# print("hello")
# sys.stderr.write("world\n")
# captured = capsys.readouterr()
# assert captured.out == "hello\n"
# assert captured.err == "world\n"
# print("next")
# captured = capsys.readouterr()
# assert captured.out == "next\n"


# @pytest.fixture
# def testingDb():
#     return db


def test_insertingUser(capsys, testingApp):

    # allUsers = User.query.all()
    # print("allUsers")
    with capsys.disabled():
        with testingApp.app_context():
            print("the database url is: ", os.environ.get("TESTING_DB"))
            print(User.query.all())
            user = User(email="dummyemail@email.com", password="fakepassword")
            db.session.add(user)
            db.session.commit()

            queriedUser = User.query.filter_by(
                email="dummyemail@email.com", password="fakepassword"
            ).first()
            print(queriedUser.email, queriedUser.password)
            assert queriedUser is not None
            assert queriedUser.email == "dummyemail@email.com"
            assert queriedUser.password == "fakepassword"

            db.session.delete(queriedUser)
            db.session.commit()

        # user = User(email='dummyemail@email.com' password='fakepassword')
        # deleteAllUnverifiedUsers()
        # with testingApp.app_context():
        #     print(os.environ.get("SQLALCHEMY_DATABASE_URI"))
        #     # print("before applying config: ", testingApp.config)
        #     # testingApp.config.from_object(Config)
        #     # print("after applying config: ", testingApp.config)
        #     print("hello!")
    print("hi!")
    # assert (1 + 1) == 2
    # user = User(email='dummyemail@email.com' password='fakepassword')
    # deleteAllUnverifiedUsers()
