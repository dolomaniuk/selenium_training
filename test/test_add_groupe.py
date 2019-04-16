# -*- coding: utf-8 -*-
import pytest

from model.group import Group


def test_add_groupe(app):
    app.group.create(Group(name="new_group", logo="new_logo", comment="new_comment"))

# @pytest.mark.skip
def test_add_empty_groupe(app):
    app.group.create(Group(name="", logo="", comment=""))

