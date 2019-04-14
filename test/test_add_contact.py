# -*- coding: utf-8  -*-

import pytest
from fixture.application import Application
from model.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")

    new_client = Contact(
            address="Sovetskaya 32",
            firstname="Dmitry",
            middlename="Ivanov",
            lastname="Pupkin",
            nickname="pupa"
            )
    app.contact.add_contact(new_client)
