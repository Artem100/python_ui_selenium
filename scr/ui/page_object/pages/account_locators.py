from selenium.webdriver.common.by import By

from scr.ui.page_object.pages.page_elements import PageElements


class AccountPage(PageElements):


    PROFILE_SECTION_BUTTON = (By.CSS_SELECTOR, "div#tabs>ul>li:nth-child(2)>a", "PROFILE SECTION BUTTON")
    INTERESTS_FIELD_EDIT = (By.CSS_SELECTOR, "textarea#description", "INTERESTS FIELD EDIT")
    INTERESTS_FIELD_CHECK_VALUE = (By.CSS_SELECTOR, "a[href*='/users/hobby/']", "INTERESTS FIELD CHECK VALUE")


    def profile_section_button_click(self):
        self.click(*self.PROFILE_SECTION_BUTTON)
        return self

    def interests_field_input(self, interest):
        self.clear_and_input_text(interest, *self.INTERESTS_FIELD_EDIT)
        return self

