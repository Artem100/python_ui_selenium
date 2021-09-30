from selenium.webdriver.common.by import By

from scr.ui.page_object.base_page import BasePage


class AccountPage(BasePage):

    LOGOUT_BUTTON = (By.CSS_SELECTOR, "span.logout a", "LOGOUT BUTTON")
    PROFILE_BUTTON = (By.CSS_SELECTOR, "span.my_profile a", "PROFILE BUTTON")
    EDIT_BUTTON = (By.CSS_SELECTOR, "div.usr_profile_menu a[href*='editprofile.html']", "EDIT BUTTON")

    def logout_button_display(self):
        self._element_displayed(*self.LOGOUT_BUTTON)
        return self

    def logout_button_click(self):
        self._click(*self.LOGOUT_BUTTON)
        return self

    def profile_button_click(self):
        self._click(*self.PROFILE_BUTTON)
        return self

    def editbutton_click(self):
        self._click(*self.EDIT_BUTTON)
        return self

