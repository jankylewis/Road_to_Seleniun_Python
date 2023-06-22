from selenium.webdriver.common.by import By
from spo.spofrag_epic.page_object.abstract_pom import Locator_Type as locator_type
from selenium.webdriver.remote.webelement import *


class LogInPOM:
    driver_factory = None

    def __init__(self, driver_factory):
        self.driver_factory = driver_factory

    elements_dict = {
        "TXT_EMAIL_OR_USRNAME": (By.ID, "login-username"),
        "TXT_PWD": (By.ID, "login-password"),
        "BTN_LOG_IN": (By.ID, "login-button"),
        "TG_REMEMBER_ME": "//div[@data-testid = 'login-container']//input[@id = 'login-remember']//parent::label",
        "TG_REMEMBER_ME_DF_CHECKED": "//div[@data-testid = 'login-container']//input[@id = 'login-remember']"
    }

    def get_tg_remember_me(self) -> WebElement:
        return self.driver_factory.find_element(locator_type.get_xpath_type(),
                                                LogInPOM.elements_dict.get("TG_REMEMBER_ME"))

    def get_tg_remember_me_df_checked(self) -> WebElement:
        return self.driver_factory.find_element(locator_type.get_xpath_type(),
                                                LogInPOM.elements_dict.get("TG_REMEMBER_ME_DF_CHECKED"))
