from selenium.webdriver.common.by import By

from src.ui.page_object.base_page import BasePage
from src.ui.page_object.pages.page_elements import PageElements


class LoginPageLocators(PageElements):

    LOGIN_PAGE_URL = "ucp.php?mode=login"
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login", "LOGIN FORM")
    LOGIN_FIELD = (By.CSS_SELECTOR, "input#username", "LOGIN FIELD")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input#password", "PASSWORD FIELD")
    SUBMIT_LOGIN_BUTTON = (By.CSS_SELECTOR, "input[name='login']", "SUBMIT BUTTON")


    def login_page_open(self, url):
        self.open_page_via_url(url+self.LOGIN_PAGE_URL)
        return self

    def login_form_display(self):
        self.element_displayed(*self.LOGIN_FORM)
        return self

    def login_field_input(self, value):
        self.element_displayed(*self.LOGIN_FIELD)
        self.input_text(value, *self.LOGIN_FIELD)
        return self

    def password_field(self, value):
        self.input_text(value, *self.PASSWORD_FIELD)
        return self

    def login_submit_button_click(self):
        self.click(*self.SUBMIT_LOGIN_BUTTON)
        return self