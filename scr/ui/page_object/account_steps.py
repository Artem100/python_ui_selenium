import allure

from scr.ui.page_object.pages.account_locators import AccountPage


class AccountSteps(AccountPage):

    @allure.step("Edit info at profile")
    def edit_info_at_profile(self, interest):
        self.interests_field_input(interest)

    @allure.step("Go to profile page")
    def go_to_profile_page(self):
        self.profile_section_button_click()