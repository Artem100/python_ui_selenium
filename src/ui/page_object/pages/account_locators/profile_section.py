from selenium.webdriver.common.by import By

from src.ui.page_object.pages.account_locators.account_root_locators import AccountRoot


class ProfileSectionLocators(AccountRoot):


    PERSONAL_INFO_BUTTON_ACIVE = (By.CSS_SELECTOR, "li.active-subsection.active-subsection", "PERSONAL INFO BUTTON ACIVE")
    INTERESTS_FIELD = (By.CSS_SELECTOR, "textarea#pf_phpbb_interests", "INTERESTS FIELD")
    OCCUPATION_FIELD = (By.CSS_SELECTOR, "textarea#pf_phpbb_occupation", "OCCUPATION FIELD")
    ICQ_FIELD = (By.CSS_SELECTOR, "input#pf_phpbb_icq", "ICQ FIELD")
    WEBSITE_FIELD = (By.CSS_SELECTOR, "input#pf_phpbb_website", "WEBSITE FIELD")
    YAHOO_FIELD = (By.CSS_SELECTOR, "input#pf_phpbb_yahoo", "WEBSITE FIELD")
    AOL_FIELD = (By.CSS_SELECTOR, "input#pf_phpbb_aol", "AOL FIELD")
    LOCATION_FIELD = (By.CSS_SELECTOR, "input#pf_phpbb_location", "LOCATION FIELD")
    FACEBOOK_FIELD = (By.CSS_SELECTOR, "input#pf_phpbb_facebook", "FACEBOOK FIELD")
    SKYPE_FIELD = (By.CSS_SELECTOR, "input#pf_phpbb_skype", "SKYPE FIELD")
    TWITTER_FIELD = (By.CSS_SELECTOR, "input#pf_phpbb_twitter", "TWITTER FIELD")
    YOUTUBE_FIELD = (By.CSS_SELECTOR, "input#pf_phpbb_youtube", "YOUTUBE FIELD")

    def interests_field_input(self, value):
        self.clear_and_input_text(value, *self.INTERESTS_FIELD)
        return self

    def interests_field_check_value(self, value):
        self.check_text_in_element(value, *self.INTERESTS_FIELD)
        return self

    def occupation_field_input(self, value):
        self.clear_and_input_text(value, *self.OCCUPATION_FIELD)
        return self

    def occupation_field_check_value(self, value):
        self.check_text_in_element(value, *self.OCCUPATION_FIELD)
        return self

    def icq_field_input(self, value):
        self.clear_and_input_text(value, *self.ICQ_FIELD)
        return self

    def icq_field_check_value(self, value):
        self.check_attribute_value_in_element(value, *self.ICQ_FIELD)
        return self

    def website_field_input(self, value):
        self.clear_and_input_text(value, *self.WEBSITE_FIELD)
        return self

    def website_field_check_value(self, value):
        self.check_attribute_value_in_element(value, *self.WEBSITE_FIELD)
        return self

    def yahoo_field_input(self, value):
        self.clear_and_input_text(value, *self.YAHOO_FIELD)
        return self

    def yahoo_field_check_value(self, value):
        self.check_attribute_value_in_element(value, *self.YAHOO_FIELD)
        return self

    def aol_field_input(self, value):
        self.clear_and_input_text(value, *self.AOL_FIELD)
        return self

    def aol_field_check_value(self, value):
        self.check_attribute_value_in_element(value, *self.AOL_FIELD)
        return self

    def location_field_input(self, value):
        self.clear_and_input_text(value, *self.LOCATION_FIELD)
        return self

    def location_field_check_value(self, value):
        self.check_attribute_value_in_element(value, *self.LOCATION_FIELD)
        return self

    def facebook_field_input(self, value):
        self.clear_and_input_text(value, *self.FACEBOOK_FIELD)
        return self

    def facebook_field_check_value(self, value):
        self.check_attribute_value_in_element(value, *self.FACEBOOK_FIELD)
        return self

    def skype_field_input(self, value):
        self.clear_and_input_text(value, *self.SKYPE_FIELD)
        return self

    def skype_field_check_value(self, value):
        self.check_attribute_value_in_element(value, *self.SKYPE_FIELD)
        return self

    def twitter_field_input(self, value):
        self.clear_and_input_text(value, *self.TWITTER_FIELD)
        return self

    def twitter_field_check_value(self, value):
        self.check_attribute_value_in_element(value, *self.TWITTER_FIELD)
        return self

    def youtube_field_input(self, value):
        self.clear_and_input_text(value, *self.YOUTUBE_FIELD)
        return self

    def youtube_field_check_value(self, value):
        self.check_attribute_value_in_element(value, *self.YOUTUBE_FIELD)
        return self

    def personal_info_button_active(self):
        self.element_displayed(*self.PERSONAL_INFO_BUTTON_ACIVE)
        return self



