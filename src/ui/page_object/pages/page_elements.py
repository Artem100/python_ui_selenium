from selenium.webdriver.common.by import By

from src.ui.page_object.base_page import BasePage


class PageElements(BasePage):

    SAVE_BUTTON = (By.CSS_SELECTOR, "input#save", "SAVE BUTTON")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[name='submit']", "SUBMIT BUTTON")
    MESSAGE_TITLE = (By.CSS_SELECTOR, "div#message h2", "MESSAGE TEXT")
    MESSAGE_TEXT = (By.CSS_SELECTOR, "div#message p", "MESSAGE TEXT")

    def save_button_click(self):
        self.click(*self.SAVE_BUTTON)
        return self

    def submit_button_click(self):
        self.element_displayed(*self.SUBMIT_BUTTON)
        self.click(*self.SUBMIT_BUTTON)
        return self

    def message_info_check(self, title): #, text):
        self.check_text_in_element(title, *self.MESSAGE_TITLE)
        # self.check_text_in_element(text, *self.MESSAGE_TEXT)
        return self

