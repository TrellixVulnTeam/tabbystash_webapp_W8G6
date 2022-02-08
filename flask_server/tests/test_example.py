import pytest
import os

from src import create_app
from src.extensions import db
from src.models import User
from flask import current_app


@pytest.fixture
def dummyApp():
    return create_app()


@pytest.fixture
def dummyUser():
    user = User(email="dummyemail@email.com", password="fakepassword")
    return user


@pytest.fixture
def database(dummyApp, dummyUser):
    yield db
    with dummyApp.app_context():
        db.session.delete(dummyUser)
        db.session.commit()


def test_insertingUser(capsys, database, dummyUser, dummyApp):
    with dummyApp.app_context():
        database.session.add(dummyUser)
        database.session.commit()
        queriedUser = User.query.filter_by(
            email="dummyemail@email.com", password="fakepassword"
        ).first()
        print(queriedUser.email, queriedUser.password)
        assert queriedUser is not None
        assert queriedUser.email == "dummyemail@email.com"
        assert queriedUser.password == "fakepassword"
