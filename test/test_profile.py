import allure
import pytest
from ddt import data

from src.additional_methods.data_provider import getCSVData
from variable_data import *
from src.ui.page_object.login_page_steps import LoginPageSteps
from src.ui.page_object.main_page_steps import MainPageSteps
from src.ui.page_object.pages.page_elements import PageElements
from src.ui.page_object.user_bar_steps import UserBarSteps
from src.ui.page_object.account_steps import AccountSteps


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
        # self.user_bar.profile_button_click()
        # yield
        # self.account_page.

    @allure.title("Change description at profile")
    def test_02(self):
        self.user_bar.go_to_personal_page()
        self.account_page.go_to_profile_section()
        self.account_page.edit_info_at_profile()
        self.account_page.check_info_at_profile()

    @allure.title("Change description at profile with data from csv file")
    @pytest.mark.parametrize("INTERESTS,OCCUPATION,ICQ,SITE,YAHOO,AOL,LOCATION,FACEBOOK,SKYPE,TWITTER,YOUTUBE", getCSVData())
    def test_03(self, INTERESTS,OCCUPATION,ICQ,SITE,YAHOO,AOL,LOCATION,FACEBOOK,SKYPE,TWITTER,YOUTUBE):
        self.user_bar.go_to_personal_page()
        self.account_page.go_to_profile_section()
        self.account_page.edit_info_at_profile(interest=INTERESTS,
                             occupation=OCCUPATION,
                             icq=ICQ,
                             site=SITE,
                             yahoo=YAHOO,
                             aol=AOL,
                             location=LOCATION,
                             facebook=FACEBOOK,
                             skype=SKYPE,
                             twitter=TWITTER,
                             youtube=YOUTUBE)
        self.account_page.check_info_at_profile()
