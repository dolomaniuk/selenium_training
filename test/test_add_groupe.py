# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.group import Group
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_groupe(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="new_group", logo="new_logo", comment="new_comment"))
    app.session.logout()


def test_add_empty_groupe(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", logo="", comment=""))
    app.session.logout()


