from selenium.webdriver.common.by import By

from scr.ui.page_object.pages.page_elements import PageElements


class MainPageLocators(PageElements):

    LOGIN_FORM = (By.CSS_SELECTOR, "form[action='/login']", "LOGIN FORM")
    LOGIN_FIELD = (By.CSS_SELECTOR, "input[name='login']", "LOGIN FIELD")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='pass']", "PASSWORD FIELD")
    SUBMIT_LOGIN_BUTTON = (By.CSS_SELECTOR, "form[action='/login'] input[type='submit']", "SUBMIT LOGIN BUTTON")
    OPEN_LOGIN_FORM_BUTTON = (By.CSS_SELECTOR, "div#guestAuthFormApp button", "OPEN LOGIN FORM BUTTON")

    def main_page_open(self, url):
        self.open_page_via_url(url)
        return self

    def login_form_display(self):
        self.element_displayed(*self.LOGIN_FORM)
        return self

    def login_field_input(self, value):
        self.input_text(value, *self.LOGIN_FIELD)
        return self

    def password_field(self, value):
        self.input_text(value, *self.PASSWORD_FIELD)
        return self

    def submit_login_button_click(self):
        self.click(*self.SUBMIT_LOGIN_BUTTON)
        return self

    def open_login_form_button_click(self):
        self.click(*self.OPEN_LOGIN_FORM_BUTTON)
        return self