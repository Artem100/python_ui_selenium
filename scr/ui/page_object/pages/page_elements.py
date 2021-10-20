from selenium.webdriver.common.by import By

from scr.ui.page_object.base_page import BasePage


class PageElements(BasePage):

    SAVE_BUTTON = (By.CSS_SELECTOR, "input#save", "SAVE BUTTON")

    def save_button_click(self):
        self.click(*self.SAVE_BUTTON)
        return self