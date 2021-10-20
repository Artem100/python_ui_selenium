import allure

from scr.ui.page_object.pages.user_bar_locators import UserBar


class UserBarSteps(UserBar):

    @allure.step("User was login")
    def user_was_login(self):
        self.logout_button_display()