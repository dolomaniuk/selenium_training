class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_address_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("ADD_NEW").click()

    def add_contact(self, contact):
        wd = self.app.wd
        self.open_add_address_page()
        # page with address field
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        # go to next page
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()
        # set firstname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        # set middlename
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        # set lastname
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # set nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # go to next page
        wd.find_element_by_name("submit").click()
        # TODO: wait show home page

    def del_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # click DELETE
        wd.find_element_by_css_selector("input[onclick=\"DeleteSel()\"]").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]")) > 0
