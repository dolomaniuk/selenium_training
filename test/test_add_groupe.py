# -*- coding: utf-8 -*-

import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_groupe(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="new_group", logo="new_logo", comment="new_comment"))
    app.logout()


def test_add_empty_groupe(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", logo="", comment=""))
    app.logout()
