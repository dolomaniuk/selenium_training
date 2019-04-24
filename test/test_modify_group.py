from random import randrange

import pytest
from model.group import Group


@pytest.mark.skip(reason="Invalid ID.")
def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="test_group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

@pytest.mark.skip(reason="Invalid ID.")
def test_modify_group_logo(app):
    if app.group.count() == 0:
        app.group.create(Group(logo="test_group"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="test_group")
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)