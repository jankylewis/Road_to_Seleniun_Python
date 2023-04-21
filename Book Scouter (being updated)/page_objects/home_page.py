from locators.home_page import HomePage as home
from selenium.webdriver.common.by import By
from common.common_waitings import CommonWaitings as common_waitings
from common.common_ui_actions import CommonUIActions as common_ui_actions
from common.common_assertions import CommonAssertions as common_assertions
from common.constants import Constants


class HomePage:
    BTN_LOG_IN = home.BTN_LOG_IN
    BTN_ACCOUNT_ICON = home.BTN_ACCOUNT_ICON
    DDI_ACCOUNT = home.DDI_ACCOUNT
    ALE_TOAST_LOGGED_IN_SUCCESSFULLY = home.ALE_TOAST_SUCCESSFULLY_LOGGED_IN

    def __init__(self, driver):
        self.driver = driver

    def click_log_in_btn(self):
        common_waitings.wait_element_until_clickable(self, HomePage.BTN_LOG_IN, Constants.TIME_OUT_3S)
        common_ui_actions.click_on_element(self, HomePage.BTN_LOG_IN)

    def click_account_icon(self):
        common_waitings.wait_element_until_clickable(self, HomePage.BTN_ACCOUNT_ICON, Constants.TIME_OUT_3S)
        common_ui_actions.click_on_element(self, HomePage.BTN_ACCOUNT_ICON)

    def click_account_ddi(self):
        common_waitings.wait_element_until_clickable(self, HomePage.DDI_ACCOUNT, Constants.TIME_OUT_3S)
        common_ui_actions.click_on_element(self, HomePage.DDI_ACCOUNT)

    def verify_toast_is_visible(self) -> bool:
        return common_assertions.verify_element_is_visible(self, HomePage.ALE_TOAST_LOGGED_IN_SUCCESSFULLY)
