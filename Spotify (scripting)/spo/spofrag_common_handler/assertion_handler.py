from spo.spofrag_common_handler.commonfrag_constant.constant import Constant as const
from spo.spofrag_common_handler.wait_handler import WaitHandler as waiter
from selenium.webdriver.remote.webelement import *
from selenium.webdriver.common.by import By


class AssertionHandler:
    driver_factory = None

    def __init__(self, driver_factory):
        self.driver_factory = driver_factory

    def verify_element_is_visible(self, exp_element: WebElement) -> bool:
        exp_element = waiter.wait_element_until_visible(self, exp_element, const.TIME_OUT_3S)
        return exp_element.is_displayed()

    @staticmethod
    def verify_string_is_equal(exp_str: str, act_str: str) -> bool:
        if exp_str is None or act_str is None:
            print(f"There was a null value between: {exp_str} and {act_str}")
            return False
        elif exp_str.strip().casefold() == act_str.strip().casefold():
            print(f"{exp_str} was equal to {act_str}")
            return True
        else:
            print(f"Expected {exp_str} to be equal to {act_str} but found False")
            return False

    @staticmethod
    def verify_string_is_contained(exp_str: str, str_to_be_contained: str) -> bool:
        if str_to_be_contained in exp_str:
            print(f"{exp_str} contained {str_to_be_contained}")
            return True
        else:
            print(f"Expected {exp_str} to contain {str_to_be_contained} but found False")
            return False

    def is_displayed(self, exp_element: By) -> bool:
        exp_element = waiter.wait_element_until_visible(self.driver_factory, exp_element, const.TIME_OUT_3S)
        return exp_element.is_selected()
