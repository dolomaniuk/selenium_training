# -*- coding: utf-8 -*-
import pytest

from model.group import Group


def test_add_groupe(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="new_group", logo="new_logo", comment="new_comment"))
    app.session.logout()


@pytest.mark.skip
def test_add_empty_groupe(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", logo="", comment=""))
    app.session.logout()


