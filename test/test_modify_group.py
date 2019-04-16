import pytest
from model.group import Group


# @pytest.mark.skip(reason="Not working functional")
def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_group"))
    app.group.modify_first_group(Group(name="New group name"))


# @pytest.mark.skip(reason="Not working functional")
def test_modify_group_logo(app):
    if app.group.count() == 0:
        app.group.create(Group(logo="test_group"))
    app.group.modify_first_group(Group(logo="New logo"))
