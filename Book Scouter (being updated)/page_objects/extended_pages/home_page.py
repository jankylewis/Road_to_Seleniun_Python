from common.common_assertions import CommonAssertions as common_assertions
from common.common_ui_actions import CommonUIActions as common_ui_actions
from common.common_waitings import CommonWaitings as common_waitings
from common.constants import Constants
from locators.extended_pages.home_page import HomePage as home


class HomePage:
    BTN_LOG_IN = home.BTN_LOG_IN
    BTN_ACCOUNT_ICON = home.BTN_ACCOUNT_ICON
    DDI_ACCOUNT = home.DDI_ACCOUNT
    ALE_TOAST_LOGGED_IN_SUCCESSFULLY = home.ALE_TOAST_SUCCESSFULLY_LOGGED_IN
    BTN_SIGN_UP = home.BTN_SIGN_UP

    def __init__(self, driver):
        self.driver = driver

    def click_log_in_btn(self):
        common_waitings.wait_element_until_clickable(self, HomePage.BTN_LOG_IN, Constants.TIME_OUT_3S)
        common_ui_actions.click_on_element(self, HomePage.BTN_LOG_IN)

    def click_sign_up_btn(self) -> object:
        """

        :rtype: object
        """
        common_waitings.wait_element_until_clickable(self, HomePage.BTN_SIGN_UP, Constants.TIME_OUT_3S)
        common_ui_actions.click_on_element(self, HomePage.BTN_SIGN_UP)

    def click_account_icon(self):
        common_waitings.wait_element_until_clickable(self, HomePage.BTN_ACCOUNT_ICON, Constants.TIME_OUT_3S)
        common_ui_actions.click_on_element(self, HomePage.BTN_ACCOUNT_ICON)

    def click_account_ddi(self):
        common_waitings.wait_element_until_clickable(self, HomePage.DDI_ACCOUNT, Constants.TIME_OUT_3S)
        common_ui_actions.click_on_element(self, HomePage.DDI_ACCOUNT)

    def __verify_toast_is_visible(self) -> bool:
        return common_assertions.verify_element_is_visible(self, HomePage.ALE_TOAST_LOGGED_IN_SUCCESSFULLY)

    def __verify_toast_content(self) -> bool:
        act_content = common_ui_actions.get_text_from_element(self, HomePage.ALE_TOAST_LOGGED_IN_SUCCESSFULLY)
        return common_assertions.verify_string_is_equal(exp_str=Constants.SUCCESSFULLY_LOG_IN, act_str=act_content)

    def verify_toast(self) -> bool:
        if HomePage.__verify_toast_is_visible(self) and HomePage.__verify_toast_content(self):
            print("Toast SUCCESSFULLY verified.")
            return True
        else:
            print("Toast verified FAILED.")
            return False


