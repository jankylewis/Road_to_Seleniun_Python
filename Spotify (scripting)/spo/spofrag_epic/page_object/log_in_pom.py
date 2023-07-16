from spo.spofrag_epic.page_object.abstract_pom import LocatorType as locator_type
from selenium.webdriver.remote.webelement import *
from spo.spofrag_common_handler.assertion_handler import AssertionHandler as asserter
from spo.spofrag_common_handler.commonfrag_constant.constant import Constant as const


class LogInPOM:
    driver_factory = None

    def __init__(self, driver_factory):
        self.driver_factory = driver_factory

    elements_dict = {
        "TXT_EMAIL_OR_USRNAME": (locator_type.get_id_type(), "login-username"),
        "TXT_PWD": (locator_type.get_id_type(), "login-password"),
        "BTN_LOG_IN": (locator_type.get_id_type(), "login-button"),
        "TG_REMEMBER_ME": (
            locator_type.get_xpath_type(),
            "//div[@data-testid = 'login-container']//input[@id = 'login-remember']//parent::label",
        ),
        "TG_REMEMBER_ME_DF_CHECKED": (
            locator_type.get_xpath_type(),
            "//div[@data-testid = 'login-container']//input[@id = 'login-remember']",
        ),
        "TXT_ERR_MSG_OF_WRONG_PWD": (locator_type.get_xpath_type(), "//span[contains(@class, 'Message')]")
    }

    def get_txt_err_msg_of_wrong_pwd(self) -> WebElement:
        if asserter.verify_element_is_visible(self.driver_factory,
                                              exp_element=LogInPOM.elements_dict.get("TXT_ERR_MSG_OF_WRONG_PWD"),
                                              time_out=const.TIME_OUT_10S,
                                              is_long_wait=True):

            return LogInPOM.elements_dict.get("TXT_ERR_MSG_OF_WRONG_PWD")

    def get_tg_remember_me(self) -> WebElement:
        if asserter.verify_element_is_visible(self.driver_factory, LogInPOM.elements_dict.get("TG_REMEMBER_ME")):
            return LogInPOM.elements_dict.get("TG_REMEMBER_ME")

    def get_tg_remember_me_df_checked(self) -> WebElement:
        if asserter.verify_element_is_visible(self.driver_factory,
                                              LogInPOM.elements_dict.get("TG_REMEMBER_ME_DF_CHECKED")):
            return LogInPOM.elements_dict.get("TG_REMEMBER_ME_DF_CHECKED")

    def get_txt_email_or_username(self) -> WebElement:
        if asserter.verify_element_is_visible(self.driver_factory, LogInPOM.elements_dict.get("TXT_EMAIL_OR_USRNAME")):
            return LogInPOM.elements_dict.get("TXT_EMAIL_OR_USRNAME")

    def get_txt_password(self) -> WebElement:
        if asserter.verify_element_is_visible(self.driver_factory, LogInPOM.elements_dict.get("TXT_PWD")):
            return LogInPOM.elements_dict.get("TXT_PWD")

    def get_btn_login(self) -> WebElement:
        if asserter.verify_element_is_visible(self.driver_factory, LogInPOM.elements_dict.get("BTN_LOG_IN")):
            return LogInPOM.elements_dict.get("BTN_LOG_IN")
