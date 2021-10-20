from selenium.webdriver.common.by import By

from scr.ui.page_object.pages.page_elements import PageElements


class EditAccountPage(PageElements):

    INTERESTS_FIELD_EDIT = (By.CSS_SELECTOR, "textarea#description", "INTERESTS FIELD EDIT")
    INTERESTS_FIELD_CHECK_VALUE = (By.CSS_SELECTOR, "a[href*='/users/hobby/']", "INTERESTS FIELD CHECK VALUE")


    def interests_field_input(self, interest):
        self._clear_and_input_text(interest, *self.INTERESTS_FIELD_EDIT)
        return self

