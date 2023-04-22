from common.common_assertions import CommonAssertions as common_assertions
from common.common_ui_actions import CommonUIActions as common_ui_actions
from common.constants import Constants as const
from locators.log_in_page import LogInPage as log_in


class LogInPage:
    TXT_EMAIL: str = log_in.TXT_EMAIL
    TXT_PASSWORD: str = log_in.TXT_PASSWORD
    BTN_LOG_IN: str = log_in.BTN_LOG_IN
    ALE_TOAST_INCORRECT_PASSWORD: str = log_in.ALE_TOAST_INVALID_PASSWORD
    ALE_TOAST_BAD_CREDENTIALS: str = log_in.ALE_TOAST_BAD_CREDENTIALS
    LBL_INPUT_EMAIL_ERR_MSG: str = log_in.LBL_INPUT_EMAIL_ERR_MSG
    LBL_INPUT_PWD_ERR_MSG: str = log_in.LBL_INPUT_PWD_ERR_MSG
    LBL_INVALID_EMAIL_ERR_MSG: str = log_in.LBL_INVALID_EMAIL_ERR_MSG

    def __init__(self, driver):
        self.driver = driver

    def set_user_email(self, user_email):
        common_ui_actions.send_key_to_element(self, LogInPage.TXT_EMAIL, user_email)

    def set_user_password(self, user_password):
        common_ui_actions.send_key_to_element(self, LogInPage.TXT_PASSWORD, user_password)

    def click_log_in_btn(self):
        common_ui_actions.click_on_element(self, LogInPage.BTN_LOG_IN)

    # methods for assertions
    def verify_bad_credentials_toast_is_presented(self) -> bool:
        if common_assertions.verify_element_is_visible(self, LogInPage.ALE_TOAST_BAD_CREDENTIALS):
            exp_err_msg: str = const.BAD_CREDENTIALS
            act_err_msg: str = common_ui_actions.get_text_from_element(self, LogInPage.ALE_TOAST_BAD_CREDENTIALS)
            if common_assertions.verify_string_is_equal(exp_err_msg, act_err_msg):
                return True
            else:
                return False
        else:
            return False

    def verify_invalid_password_toast_is_presented(self) -> bool:
        if common_assertions.verify_element_is_visible(self, LogInPage.ALE_TOAST_INCORRECT_PASSWORD):
            exp_err_msg: str = const.INVALID_PASSWORD
            act_err_msg: str = common_ui_actions.get_text_from_element(self, LogInPage.ALE_TOAST_INCORRECT_PASSWORD)
            if common_assertions.verify_string_is_equal(exp_err_msg, act_err_msg):
                return True
            else:
                return False
        else:
            return False

    def verify_input_email_err_msg(self) -> bool:
        if common_assertions.verify_element_is_visible(self, LogInPage.LBL_INPUT_EMAIL_ERR_MSG):
            exp_err_msg: str = const.INPUT_EMAIL_ERR_MSG
            act_err_msg: str = common_ui_actions.get_text_from_element(self, LogInPage.LBL_INPUT_EMAIL_ERR_MSG)
            if common_assertions.verify_string_is_equal(exp_err_msg, act_err_msg):
                return True
            else:
                return False
        else:
            return False

    def verify_input_pwd_err_msg(self) -> bool:
        if common_assertions.verify_element_is_visible(self, LogInPage.LBL_INPUT_PWD_ERR_MSG):
            exp_err_msg: str = const.INPUT_PWD_ERR_MSG
            act_err_msg: str = common_ui_actions.get_text_from_element(self, LogInPage.LBL_INPUT_PWD_ERR_MSG)
            if common_assertions.verify_string_is_equal(exp_err_msg, act_err_msg):
                return True
            else:
                return False
        else:
            return False

    def verify_invalid_email_err_msg(self) -> bool:
        if common_assertions.verify_element_is_visible(self, LogInPage.LBL_INVALID_EMAIL_ERR_MSG):
            exp_err_msg: str = const.INVALID_EMAIL_ERR_MSG
            act_err_msg: str = common_ui_actions.get_text_from_element(self, LogInPage.LBL_INVALID_EMAIL_ERR_MSG)
            if common_assertions.verify_string_is_equal(exp_err_msg, act_err_msg):
                return True
            else:
                return False
        else:
            return False
