import pytest

from model.contact import Contact

@pytest.mark.skip
def test_del_contact(app):
    app.contact.del_first_contact()