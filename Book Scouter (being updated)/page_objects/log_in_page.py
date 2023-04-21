from locators.log_in_page import LogInPage as log_in
from selenium.webdriver.common.by import By
from common.common_ui_actions import CommonUIActions as common_ui_actions
from common.common_assertions import CommonAssertions as common_assertions
from common.constants import Constants as const


class LogInPage:
    TXT_EMAIL = log_in.TXT_EMAIL
    TXT_PASSWORD = log_in.TXT_PASSWORD
    BTN_LOG_IN = log_in.BTN_LOG_IN
    ALE_TOAST_INCORRECT_PASSWORD = log_in.ALE_TOAST_INVALID_PASSWORD
    ALE_TOAST_BAD_CREDENTIALS = log_in.ALE_TOAST_BAD_CREDENTIALS

    def __init__(self, driver):
        self.driver = driver

    def set_user_email(self, user_email):
        common_ui_actions.send_key_to_element(self, LogInPage.TXT_EMAIL, user_email)

    def set_user_password(self, user_password):
        common_ui_actions.send_key_to_element(self, LogInPage.TXT_PASSWORD, user_password)

    def click_log_in_btn(self):
        common_ui_actions.click_on_element(self, LogInPage.BTN_LOG_IN)

    def verify_bad_credentials_errmsg_is_presented(self) -> bool:
        if common_assertions.verify_element_is_visible(self, LogInPage.ALE_TOAST_BAD_CREDENTIALS):
            exp_errmsg: str = const.BAD_CREDENTIALS
            act_errmsg: str = common_ui_actions.get_text_from_element(self, LogInPage.ALE_TOAST_BAD_CREDENTIALS)
            if common_assertions.verify_string_is_equal(exp_errmsg, act_errmsg):
                return True
            else:
                return False

    def verify_invalid_password_errmsg_is_presented(self):
        if common_assertions.verify_element_is_visible(self, LogInPage.ALE_TOAST_INCORRECT_PASSWORD):
            exp_errmsg: str = const.INVALID_PASSWORD
            act_errmsg: str = common_ui_actions.get_text_from_element(self, LogInPage.ALE_TOAST_INCORRECT_PASSWORD)
            if common_assertions.verify_string_is_equal(exp_errmsg, act_errmsg):
                return True
            else:
                return False
