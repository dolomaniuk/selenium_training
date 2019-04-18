# -*- coding: utf-8 -*-

import pytest

from model.group import Group


def test_add_groupe(app):
    old_groups = app.group.get_group_list()
    group = Group(name="new_group", logo="new_logo", comment="new_comment")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



# @pytest.mark.skip
def test_add_empty_groupe(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", logo="", comment="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

