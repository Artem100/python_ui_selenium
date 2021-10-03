import allure

from scr.ui.page_object.pages.edit_account_locators import EditAccountPage


class EditAccountSteps(EditAccountPage):

    @allure.step("Edit info at profile")
    def edit_info_at_profile(self, interest):
        self.interests_field_input(interest)