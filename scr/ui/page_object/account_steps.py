import allure

from scr.ui.page_object.pages.account_page import AccountPage


class AccountSteps(AccountPage):

    @allure.step("User was login")
    def user_was_login(self):
        self.logout_button_display()

