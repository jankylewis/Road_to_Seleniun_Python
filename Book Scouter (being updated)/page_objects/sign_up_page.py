# may use
from common.common_ui_actions import CommonUIActions as common_ui_actions
from common.common_assertions import CommonAssertions as common_assertions
from common.constants import Constants as const
from locators.sign_up_page import SignUpPage as sign_up


class SignUpPage:
    TXT_EMAIL: str = sign_up.TXT_EMAIL
    TXT_PASSWORD: str = sign_up.TXT_PASSWORD
    BTN_SIGN_UP: str = sign_up.BTN_SIGN_UP
    CHK_NEWSLETTER: str = sign_up.CHK_NEWSLETTER
    CHK_BECOME_PRO: str = sign_up.CHK_BECOME_PRO
    BTN_LOG_IN: str = sign_up.BTN_LOG_IN
    LBL_PRO: str = sign_up.LBL_PRO
    IMG_HANDSHAKE: str = sign_up.IMG_HANDSHAKE
    IMG_COUNT: str = sign_up.IMG_COUNT
    IMG_CLOCK: str = sign_up.IMG_CLOCK
    IMG_MONEY: str = sign_up.IMG_MONEY
    IMG_CALENDAR: str = sign_up.IMG_CALENDAR
    TXT_CC_NUMBER: str = sign_up.TXT_CC_NUMBER
    TXT_EXPIRED_DATE: str = sign_up.TXT_EXPIRED_DATE
    TXT_CVC: str = sign_up.TXT_CVC
    BTN_REGISTER_CARD: str = sign_up.BTN_REGISTER_CARD
    LBL_INVALID_CC_NUMBER: str = sign_up.LBL_INVALID_CC_NUMBER
    LBL_INVALID_EXPIRED_DATE: str = sign_up.LBL_INVALID_EXPIRED_DATE
    LBL_INVALID_CVC: str = sign_up.LBL_INVALID_CVC
    LBL_INPUT_EMAIL_ERR_MSG: str = sign_up.LBL_INPUT_EMAIL_ERR_MSG
    LBL_INPUT_PWD_ERR_MSG: str = sign_up.LBL_INPUT_PWD_ERR_MSG
    LBL_INVALID_EMAIL_ERR_MSG: str = sign_up.LBL_INVALID_EMAIL_ERR_MSG
    LBL_INVALID_PWD_ERR_MSG: str = sign_up.LBL_INVALID_PWD_ERR_MSG
    ALE_TOAST_EXISTED_EMAIL: str = sign_up.ALE_TOAST_EXISTED_EMAIL

    def __init__(self, driver):
        self.driver = driver

    # register as a pro flow
    def set_cc_number(self, exp_cc_number):
        common_ui_actions.send_key_to_element(self, SignUpPage.TXT_CC_NUMBER, exp_cc_number)

    def set_expired_date(self, exp_expired_date):
        common_ui_actions.send_key_to_element(self, SignUpPage.TXT_EXPIRED_DATE, exp_expired_date)

    def set_cvc(self, exp_cvc):
        common_ui_actions.send_key_to_element(self, SignUpPage.TXT_CVC, exp_cvc)

    # register as a basic user flow
    def set_user_email(self, exp_user_email):
        common_ui_actions.send_key_to_element(self, SignUpPage.TXT_EMAIL, exp_user_email)

    def set_user_password(self, exp_user_pwd):
        common_ui_actions.send_key_to_element(self, SignUpPage.TXT_PASSWORD, exp_user_pwd)

    def check_newsletter(self):
        common_ui_actions.click_on_element(self, SignUpPage.CHK_NEWSLETTER)

    def check_becoming_pro(self):
        common_ui_actions.click_on_element(self, SignUpPage.CHK_BECOME_PRO)

    def click_sign_up_btn(self):
        common_ui_actions.click_on_element(self, SignUpPage.BTN_SIGN_UP)

    def click_log_in_btn(self):
        common_ui_actions.click_on_element(self, SignUpPage.BTN_LOG_IN)

    def click_register_card(self):
        common_ui_actions.click_on_element(self, SignUpPage.BTN_REGISTER_CARD)

    # method to do register basically
    def execute_register(self, exp_user_email, exp_user_pwd):
        SignUpPage.set_user_email(self, exp_user_email)
        SignUpPage.set_user_password(self, exp_user_pwd)
        SignUpPage.click_sign_up_btn(self)

    # method to do register as a privileged pro flow
    def execute_register_as_pro(self, exp_cc_number, exp_expired_date, exp_cvc):
        SignUpPage.set_cc_number(self, exp_cc_number)
        SignUpPage.set_expired_date(self, exp_expired_date)
        SignUpPage.set_cvc(self, exp_cvc)
        SignUpPage.click_register_card(self)

    # assertions for pro-user
    def verify_register_pro_lbl(self) -> bool:
        return common_assertions.verify_element_is_visible(self, SignUpPage.LBL_PRO)

    def verify_cc_number_err_msg(self) -> bool:
        if common_assertions.verify_element_is_visible(self, SignUpPage.LBL_INVALID_CC_NUMBER):
            print("Error message found when User has NOT provided the cc number.")
            exp_err_msg: str = const.INVALID_CC_NUMBER
            act_err_msg: str = common_ui_actions.get_text_from_element(self, SignUpPage.LBL_INVALID_CC_NUMBER)
            if common_assertions.verify_string_is_equal(exp_err_msg, act_err_msg):
                print("Error message SUCCESSFULLY verified when User has NOT provided the cc number.")
                return True
            else:
                print("Error message verified FAILED when User has NOT provided the cc number.")
                return False
        else:
            print("Error message found when User has NOT provided the cc number.")
            return False

    def verify_expired_date_err_msg(self) -> bool:
        if common_assertions.verify_element_is_visible(self, SignUpPage.LBL_INVALID_EXPIRED_DATE):
            print("Error message found when User has NOT provided the expiration date of cc.")
            exp_err_msg: str = const.INVALID_EXPIRED_DATE
            act_err_msg: str = common_ui_actions.get_text_from_element(self, SignUpPage.LBL_INVALID_EXPIRED_DATE)
            if common_assertions.verify_string_is_equal(exp_err_msg, act_err_msg):
                print("Error message SUCCESSFULLY verified when User has NOT provided the expiration date of cc.")
                return True
            else:
                print("Error message verified FAILED when User has NOT provided the expiration date of cc.")
                return False
        else:
            print("Error message found when User has NOT provided the expiration date of cc.")
            return False

    def verify_cvc_err_msg(self) -> bool:
        if common_assertions.verify_element_is_visible(self, SignUpPage.LBL_INVALID_CVC):
            print("Error message found when User has NOT provided the cvc of cc.")
            exp_err_msg: str = const.INVALID_CVC
            act_err_msg: str = common_ui_actions.get_text_from_element(self, SignUpPage.LBL_INVALID_CVC)
            if common_assertions.verify_string_is_equal(exp_err_msg, act_err_msg):
                print("Error message SUCCESSFULLY verified when User has NOT provided the cvc of cc.")
                return True
            else:
                print("Error message verified FAILED when User has NOT provided the cvc of cc.")
                return False
        else:
            print("Error message NOT found when User has NOT provided the cvc of cc.")
            return False

    # assertions for normal-user
    def verify_input_email_err_msg(self) -> bool:
        if common_assertions.verify_element_is_visible(self, SignUpPage.LBL_INPUT_EMAIL_ERR_MSG):
            print("Error message found when User has NOT inputted the email.")
            exp_err_msg: str = const.INPUT_EMAIL_ERR_MSG
            act_err_msg: str = common_ui_actions.get_text_from_element(self, SignUpPage.LBL_INPUT_EMAIL_ERR_MSG)
            if common_assertions.verify_string_is_equal(exp_err_msg, act_err_msg):
                print("Error message SUCCESSFULLY verified when User has NOT inputted the email.")
                return True
            else:
                print("Error message verified FAILED found when User has NOT inputted the email.")
                return False
        else:
            print("Error message NOT found when User has NOT inputted the email.")
            return False

    def verify_input_pwd_err_msg(self) -> bool:
        if common_assertions.verify_element_is_visible(self, SignUpPage.LBL_INPUT_PWD_ERR_MSG):
            print("Error message found when User has NOT inputted the password.")
            exp_err_msg: str = const.INPUT_PWD_ERR_MSG
            act_err_msg: str = common_ui_actions.get_text_from_element(self, SignUpPage.LBL_INPUT_PWD_ERR_MSG)
            if common_assertions.verify_string_is_equal(exp_err_msg, act_err_msg):
                print("Error message SUCCESSFULLY verified when User has NOT inputted the password.")
                return True
            else:
                print("Error message verified FAILED when User has NOT inputted the password.")
                return False
        else:
            print("Error message NOT found even when User has NOT inputted the password.")
            return False

    def verify_invalid_email_err_msg(self) -> bool:
        if common_assertions.verify_element_is_visible(self, SignUpPage.LBL_INVALID_EMAIL_ERR_MSG):
            print("Error message of the invalid email found.")
            exp_err_msg: str = const.INVALID_EMAIL_ERR_MSG
            act_err_msg: str = common_ui_actions.get_text_from_element(self, SignUpPage.LBL_INVALID_EMAIL_ERR_MSG)
            if common_assertions.verify_string_is_equal(exp_err_msg, act_err_msg):
                print("Error message of the invalid email SUCCESSFULLY verified.")
                return True
            else:
                print("Error message of the invalid email verified FAILED.")
                return False
        else:
            print("Error message of the invalid email NOT found.")
            return False

    def verify_invalid_pwd_err_msg(self) -> bool:
        if common_assertions.verify_element_is_visible(self, SignUpPage.LBL_INVALID_PWD_ERR_MSG):
            print("Error message of the invalid password found.")
            exp_err_msg: str = const.INVALID_PWD_ERR_MSG
            act_err_msg: str = common_ui_actions.get_text_from_element(self, SignUpPage.LBL_INVALID_PWD_ERR_MSG)
            if common_assertions.verify_string_is_equal(exp_err_msg, act_err_msg):
                print("Error message of the invalid password SUCCESSFULLY verified.")
                return True
            else:
                print("Error message of the invalid password verified FAILED.")
                return False
        else:
            print("Error message of the invalid password NOT found.")
            return False

    def verify_existed_email_toast_presented(self) -> bool:
        if common_assertions.verify_element_is_visible(self, SignUpPage.ALE_TOAST_EXISTED_EMAIL):
            print("Toast found.")
            exp_err_msg: str = const.EXISTED_EMAIL
            act_err_msg: str = common_ui_actions.get_text_from_element(self, SignUpPage.ALE_TOAST_EXISTED_EMAIL)
            if common_assertions.verify_string_is_equal(exp_err_msg, act_err_msg):
                print("Toast SUCCESSFULLY verified.")
                return True
            else:
                print("Toast verified FAILED.")
                return False
        else:
            print("Toast NOT found.")
            return False
