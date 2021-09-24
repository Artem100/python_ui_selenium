import allure

from scr.ui.page_object.pages.login_page_locators import LoginPageLocators


class LoginPageSteps(LoginPageLocators):

    @allure.step("Login to profile from *Login* page")
    def login_to_profile_from_login_page(self, url, username, password):
        self.login_page_open(url)
        self.login_form_display()
        self.login_field_input(username)
        self.password_field(password)
        self.sumbit_button_click()