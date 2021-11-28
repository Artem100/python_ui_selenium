from selenium.webdriver.common.by import By

from src.ui.page_object.pages.page_elements import PageElements


class UserBar(PageElements):


    LOGOUT_BUTTON = (By.CSS_SELECTOR, "span.logout a", "LOGOUT BUTTON")
    PROFILE_BUTTON = (By.CSS_SELECTOR, "div.header-profile", "PROFILE BUTTON")
    PERSONAL_SECTION_BUTTON = (By.CSS_SELECTOR, "li#username_logged_in a[title='Личный раздел']", "PERSONAL SECTION BUTTON")

    def logout_button_display(self):
        self.element_displayed(*self.LOGOUT_BUTTON)
        return self

    def logout_button_click(self):
        self.click(*self.LOGOUT_BUTTON)
        return self

    def profile_button_click(self):
        self.click(*self.PROFILE_BUTTON)
        return self

    def personal_section_button_click(self):
        self.click(*self.PERSONAL_SECTION_BUTTON)
        return self