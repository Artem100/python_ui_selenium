from selenium.webdriver.common.by import By

from scr.ui.page_object.pages.page_elements import PageElements


class AccountPage(PageElements):


    EDIT_PROFILE_BUTTON = (By.CSS_SELECTOR, "div.usr_profile_menu a[href*='editprofile.html']", "EDIT BUTTON")
    INTERESTS_FIELD_CHECK_VALUE = (By.CSS_SELECTOR, "a[href*='/users/hobby/']", "INTERESTS FIELD CHECK VALUE")


    def edit_profile_button_click(self):
        self._click(*self.EDIT_PROFILE_BUTTON)
        return self

    def at_account_page(self):
        self._element_displayed(*self.EDIT_PROFILE_BUTTON)
        return self

    def interests_field_check_value(self, interest):
        self._check_text_in_element(interest, *self.INTERESTS_FIELD_CHECK_VALUE)
        return self

