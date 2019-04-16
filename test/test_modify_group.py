import pytest
from model.group import Group


# @pytest.mark.skip(reason="Not working functional")
def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group name"))


# @pytest.mark.skip(reason="Not working functional")
def test_modify_group_logo(app):
    app.group.modify_first_group(Group(logo="New logo"))
