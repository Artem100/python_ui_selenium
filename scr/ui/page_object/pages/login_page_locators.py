from selenium.webdriver.common.by import By

from scr.ui.page_object.base_page import BasePage


class LoginPageLocators(BasePage):

    LOGIN_PAGE_URL = "login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "table.login_form", "LOGIN FORM")
    LOGIN_FIELD = (By.CSS_SELECTOR, "input#login_field", "LOGIN FIELD")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input#pass_field", "PASSWORD FIELD")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[name='login_btn']", "SUBMIT BUTTON")


    def login_page_open(self, url):
        self.open_page_via_url(url+self.LOGIN_PAGE_URL)
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

    def submit_button_click(self):
        self._click(*self.SUBMIT_BUTTON)
        return self