from locators.sign_up_page import SignUpPage as sign_up
from selenium.webdriver.common.by import By

# may use
from common.common_ui_actions import CommonUIActions as common_ui_actions
from common.common_assertions import CommonAssertions as common_assertions
from common.constants import Constants as const


class SignUpPage:
    TXT_EMAIL: str = sign_up.TXT_EMAIL
    TXT_PASSWORD: str = sign_up.TXT_PASSWORD
    BTN_SIGN_UP: str = sign_up.BTN_SIGN_UP
    CHK_NEWSLETTER: str = sign_up.CHK_NEWSLETTER
    CHK_BECOME_PRO: str = sign_up.CHK_BECOME_PRO

    def __init__(self, driver):
        self.driver = driver

    def set_user_email(self, exp_user_email):
        pass

    def set_user_password(self, exp_user_pwd):
        pass

    def check_newsletter(self):
        pass

    def check_becoming_pro(self):
        pass

    def click_sign_up_btn(self):
        pass

    def click_log_in_btn(self):
        pass
