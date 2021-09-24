import allure

from scr.ui.page_object.pages.main_page_locators import MainPageLocators


class MainPageSteps(MainPageLocators):

    @allure.step("Login to profile")
    def login_to_profile_step(self, url, username, password):
        self.main_page_open(url)
        self.open_login_form_button_click()
        self.login_form_display()
        self.login_field_input(username)
        self.password_field(password)
        self.sumbit_button_click()