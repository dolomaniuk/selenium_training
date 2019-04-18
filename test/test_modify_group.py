import pytest
from model.group import Group


@pytest.mark.skip(reason="Not working functional")
def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="test_group")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

@pytest.mark.skip(reason="Not working functional")
def test_modify_group_logo(app):
    if app.group.count() == 0:
        app.group.create(Group(logo="test_group"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(logo="New logo"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)