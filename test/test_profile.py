import allure
import pytest

from variable_data import *
from scr.ui.page_object.account_steps import AccountSteps
from scr.ui.page_object.login_page_steps import LoginPageSteps
from scr.ui.page_object.main_page_steps import MainPageSteps
from scr.ui.page_object.pages.page_elements import PageElements
from scr.ui.page_object.user_bar_steps import UserBarSteps
from scr.ui.page_object.account_steps import AccountSteps


class TestProfile():

    @pytest.fixture(autouse=True)
    def profile_suite_setup(self, browser, faker):
        main_browser = browser
        self.main_page = MainPageSteps(main_browser)
        self.login_page = LoginPageSteps(main_browser)
        self.account_page = AccountSteps(main_browser)
        self.profile_page = AccountSteps(main_browser)
        self.user_bar = UserBarSteps(main_browser)
        self.page_elements = PageElements(main_browser)

        self.interest = faker.word()

        self.login_page.login_to_profile_from_login_page(url_env,
                                                         email_main_user,
                                                         password_user)
        self.user_bar.profile_button_click()
        # yield
        # self.account_page.

    @allure.title("Change description at profile")
    def test_02(self):
        self.user_bar.go_to_personal_page()
        self.account_page.go_to_profile_page()
        # self.profile_page.interests_field_input(self.interest)
        # self.page_elements.save_button_click()
        # self.account_page.at_account_page()
        # self.account_page.check_info_account_page(self.interest)
