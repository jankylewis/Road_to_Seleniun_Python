from selenium.webdriver.common.by import By

from common.common_waitings import CommonWaitings
from common.constants import Constants


class CommonAssertions:

    def __init__(self, driver):
        self.driver = driver

    # can modify the time-out parameter when scripting
    def verify_element_is_visible(self, exp_locator: str) -> bool:
        CommonWaitings.wait_element_until_visible(self, exp_locator, Constants.TIME_OUT_10S)
        return self.driver.find_element(By.XPATH, exp_locator).is_displayed()

    @staticmethod
    def verify_string_is_equal(exp_str: str, act_str: str) -> bool:
        """

        :param exp_str:
        :param act_str:
        :return:
        """
        if exp_str is None or act_str is None:
            print(f"There is a null value between: {exp_str} and {act_str}")
            return False
        if exp_str.casefold() == act_str.casefold():
            print(f"{exp_str} was equal to {act_str}")
            return True
        else:
            print(f"{exp_str} was not equal to {act_str}")
            return False
