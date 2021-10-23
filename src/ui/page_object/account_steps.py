import allure

from src.data_for_tests.data_fields import *
from src.ui.page_object.pages.account_locators.profile_section import ProfileSectionLocators


class AccountSteps(ProfileSectionLocators):

    @allure.step("Edit info at personal info section")
    def edit_info_at_profile(self,
                             interest=PersonalInfoData.INTERESTS,
                             occupation=PersonalInfoData.OCCUPATION,
                             icq=PersonalInfoData.ICQ,
                             site=PersonalInfoData.SITE,
                             yahoo=PersonalInfoData.YAHOO,
                             aol=PersonalInfoData.AOL,
                             location=PersonalInfoData.LOCATION,
                             facebook=PersonalInfoData.FACEBOOK,
                             skype=PersonalInfoData.SKYPE,
                             twitter=PersonalInfoData.TWITTER,
                             youtube=PersonalInfoData.YOUTUBE):
        self.interests_field_input(interest)
        self.occupation_field_input(occupation)
        self.icq_field_input(icq)
        self.website_field_input(site)
        self.yahoo_field_input(yahoo)
        self.aol_field_input(aol)
        self.location_field_input(location)
        self.facebook_field_input(facebook)
        self.skype_field_input(skype)
        self.twitter_field_input(twitter)
        self.youtube_field_input(youtube)
        self.submit_button_click()
        self.message_info_check(MESSAGE_TEXT.PROFILE_MESSAGE_TITLE)

                                # MESSAGE_TEXT.PROFILE_MESSAGE_TEXT)

    @allure.step("Go to profile page")
    def go_to_profile_section(self):
        self.profile_section_button_click()


    @allure.step("Check info at personal info section")
    def check_info_at_profile(self,
                             interest=PersonalInfoData.INTERESTS,
                             occupation=PersonalInfoData.OCCUPATION,
                             icq=PersonalInfoData.ICQ,
                             site=PersonalInfoData.SITE,
                             yahoo=PersonalInfoData.YAHOO,
                             aol=PersonalInfoData.AOL,
                             location=PersonalInfoData.LOCATION,
                             facebook=PersonalInfoData.FACEBOOK,
                             skype=PersonalInfoData.SKYPE,
                             twitter=PersonalInfoData.TWITTER,
                             youtube=PersonalInfoData.YOUTUBE):
        self.personal_info_button_active()
        self.interests_field_check_value(interest)
        self.occupation_field_check_value(occupation)
        self.icq_field_check_value(icq)
        self.website_field_check_value(site)
        self.yahoo_field_check_value(yahoo)
        self.aol_field_check_value(aol)
        self.location_field_check_value(location)
        self.facebook_field_check_value(facebook)
        self.skype_field_check_value(skype)
        self.twitter_field_check_value(twitter)
        self.youtube_field_check_value(youtube)
