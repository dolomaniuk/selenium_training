import pytest

from model.contact import Contact

@pytest.mark.skip
def test_del_contact(app):
    if app.contact.count() == 0:
        test_client = Contact(
                address="Sovetskaya 32",
                firstname="Dmitry",
                middlename="Ivanov",
                lastname="Pupkin",
                nickname="pupa"
        )
        app.contact.add_contact(test_client)
    app.contact.del_first_contact()