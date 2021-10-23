from selenium.webdriver.common.by import By

from src.ui.page_object.pages.page_elements import PageElements


class AccountRootPage(PageElements):


    PROFILE_SECTION_BUTTON = (By.CSS_SELECTOR, "div#tabs>ul>li:nth-child(2)>a", "PROFILE SECTION BUTTON")



    def profile_section_button_click(self):
        self.click(*self.PROFILE_SECTION_BUTTON)
        return self
