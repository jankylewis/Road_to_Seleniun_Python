from locators.profile_page import ProfilePage as profile_page
from selenium.webdriver.common.by import By
from common.common_assertions import CommonAssertions as common_assertions
from common.common_ui_actions import CommonUIActions as common_ui_actions
from common.constants import Constants as constants


class ProfilePage:
    LBL_USER_EMAIl = profile_page.LBL_USER_EMAIL

    def __init__(self, driver):
        self.driver = driver

    def __get_user_email(self) -> str:
        return common_ui_actions.get_text_from_element_by_attribute(self, ProfilePage.LBL_USER_EMAIl, constants.ATTRIBUTE_VALUE)

    def verify_user_email(self, exp_user_email: str) -> bool:
        return common_assertions.verify_string_is_equal(exp_user_email, ProfilePage.__get_user_email(self))



