import allure

from src.ui.page_object.pages.user_bar_locators import UserBar


class UserBarSteps(UserBar):

    @allure.step("User was login")
    def user_was_login(self):
        self.logout_button_display()

    @allure.step("Go to personal page")
    def go_to_personal_page(self):
        self.profile_button_click()
        self.personal_section_button_click()