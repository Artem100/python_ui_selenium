import allure
import pytest

import env_setup
from scr.ui.page_object.login_page_steps import LoginPageSteps
from scr.ui.page_object.main_page_steps import MainPageSteps
from scr.ui.page_object.account_steps import AccountSteps
from scr.ui.page_object.pages.user_bar_steps import UserBarSteps


class TestLogin():

    @pytest.fixture(autouse=True)
    def login_suite_setup(self, browser):
        main_browser = browser
        self.main_page = MainPageSteps(main_browser)
        self.login_page = LoginPageSteps(main_browser)
        self.account_page = AccountSteps(main_browser)
        self.user_bar = UserBarSteps(main_browser)

    @allure.title("Positive login")
    def test_01(self):
        self.login_page.login_to_profile_from_login_page(env_setup.ENV_URL,
                                                         env_setup.ENV_USER_MAIL,
                                                         env_setup.ENV_PASSWORD)
        self.user_bar.user_was_login()
