import allure

from scr.ui.page_object.pages.account_locators import AccountPage


class AccountSteps(AccountPage):

    @allure.step("Go to edit profile")
    def go_to_edit_profile(self):
        self.edit_profile_button_click()

    @allure.step("Check info account")
    def check_info_account_page(self, interests):
        self.interests_field_check_value(interests)
        return self
