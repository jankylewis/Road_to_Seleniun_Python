from selenium.common import *

from selenium.webdriver.common.keys import Keys as key
from spo.spofrag_common_handler.wait_handler import WaitHandler as waiter
from spo.spofrag_common_handler.commonfrag_constant.constant import Constant as const
from spo.spofrag_common_handler.assertion_handler import AssertionHandler as asserter
from selenium.webdriver.remote.webelement import *
from spo.spofrag_utilities.date_time_utils import DateTimeHandler as date_utils

from selenium.webdriver.common.action_chains import ActionChains as action_helper


class UIActionHandler:
    driver_factory = None

    def __init__(self, driver_factory):
        self.driver_factory = driver_factory

    def scroll_into_element_by_js(self, exp_element: WebElement):
        exp_element = waiter.wait_element_until_visible(self.driver_factory, exp_element, const.TIME_OUT_3S)
        exp_element.location_once_scrolled_into_view

    def click_until_clickable(self, exp_element: WebElement) -> bool:
        is_clickable = False
        retry = 1

        # unchangeable var
        end_min: int = date_utils.get_minute_now() + const.TIME_OUT_10S
        if exp_element:

            # UIActionHandler.scroll_into_view(self, exp_element)
            while not is_clickable and not date_utils.is_time_out(date_utils.get_date_time_now(), end_min):
                try:
                    exp_element.click()
                    is_clickable = True
                except (ElementNotInteractableException, ElementClickInterceptedException) as exception:
                    retry += 1

                if retry <= 3:
                    break
        return is_clickable

    def click_on_element(self, exp_element: WebElement) -> object:
        """

        :rtype: object
        """
        exp_element = waiter.wait_element_until_clickable(self.driver_factory, exp_element, const.TIME_OUT_3S)
        exp_element.click()

    def send_key_to_element(self, exp_element: WebElement, exp_msg: str):
        exp_element = waiter.wait_element_until_visible(self.driver_factory, exp_element, const.TIME_OUT_3S)
        UIActionHandler.click_on_element(self, exp_element)
        exp_element.clear()
        exp_element.send_keys(exp_msg)

    def get_text_from_element(self, exp_element: WebElement) -> str:
        exp_element = waiter.wait_element_until_visible(self.driver_factory, exp_element)

        return exp_element.text

    def get_value_from_element_by_attribute(self, exp_element: WebElement, attribute_name: str) -> str:
        exp_element = waiter.wait_element_until_visible(self.driver_factory, exp_element, const.TIME_OUT_3S)

        # attribute_name can be "value"
        return exp_element.get_attribute(attribute_name)

    # key pressed with element
    def press_key_by_element(self, exp_element: WebElement, key_received: str):
        exp_element = waiter.wait_element_until_visible(self.driver_factory, exp_element, const.TIME_OUT_3S)
        if asserter.verify_string_is_equal(const.KEY_ENTER, key_received):
            exp_element.send_keys(key.ENTER)

    def click_on_toggle(self, exp_toggle: WebElement, is_checked: bool = True) -> bool:
        exp_toggle = waiter.wait_element_until_visible(self.driver_factory, exp_toggle, const.TIME_OUT_3S)

        return self.driver_factory.find_element(exp_toggle).is_selected()

    def hover_over_element(self, exp_element: WebElement) -> object:
        """

        :rtype: object
        """
        exp_element = waiter.wait_element_until_clickable(self.driver_factory, exp_element, const.TIME_OUT_3S)
        action_helper(self.driver_factory).move_to_element(exp_element).perform()
