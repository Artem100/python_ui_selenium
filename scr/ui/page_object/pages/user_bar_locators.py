from selenium.webdriver.common.by import By

from scr.ui.page_object.pages.page_elements import PageElements


class UserBar(PageElements):


    LOGOUT_BUTTON = (By.CSS_SELECTOR, "span.logout a", "LOGOUT BUTTON")
    PROFILE_BUTTON = (By.CSS_SELECTOR, "div.header-profile", "PROFILE BUTTON")

    def logout_button_display(self):
        self._element_displayed(*self.LOGOUT_BUTTON)
        return self

    def logout_button_click(self):
        self._click(*self.LOGOUT_BUTTON)
        return self

    def profile_button_click(self):
        self._click(*self.PROFILE_BUTTON)
        return self