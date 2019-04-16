# -*- coding: utf-8  -*-
import pytest

from model.contact import Contact


# @pytest.mark.skip
def test_add_contact(app):
    new_client = Contact(
            address="Sovetskaya 32",
            firstname="Dmitry",
            middlename="Ivanov",
            lastname="Pupkin",
            nickname="pupa"
            )
    app.contact.add_contact(new_client)
