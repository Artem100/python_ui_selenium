from selenium.webdriver.common.by import By

from env_setup import ENV_URL
from scr.ui.page_object.base_page import BasePage


class MainPageLocators(BasePage):

    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form", "DIALOG CONTAINER")
    LOGIN_FIELD = (By.CSS_SELECTOR, "input#login", "LOGIN FIELD")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input#login_password", "PASSWORD FIELD")
    SUBMIT_LOGIN_BUTTON = (By.CSS_SELECTOR, "form#login_form button[type='submit']", "SUBMIT LOGIN BUTTON")
    OPEN_LOGIN_FORM_BUTTON = (By.CSS_SELECTOR, "div#guestAuthFormApp button", "OPEN LOGIN FORM BUTTON")

    def main_page_open(self, url):
        self.open_page_via_url(url)
        return self

    def login_form_display(self):
        self._element_displayed(*self.LOGIN_FORM)
        return self

    def login_field_input(self, value):
        self._input_text(value, *self.LOGIN_FIELD)
        return self

    def password_field(self, value):
        self._input_text(value, *self.PASSWORD_FIELD)
        return self

    def submit_login_button_click(self):
        self._click(*self.SUBMIT_LOGIN_BUTTON)
        return self

    def open_login_form_button_click(self):
        self._click(*self.OPEN_LOGIN_FORM_BUTTON)
        return self