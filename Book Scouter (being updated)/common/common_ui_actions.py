import time

import selenium.webdriver.remote.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from common.constants import Constants
from common.common_waitings import CommonWaitings
from selenium import webdriver


class CommonUIActions:

    def __init__(self, driver):
        self.driver = driver

    def maximize_popup(self: object) -> None:
        """

        :rtype: object
        """
        self.maximize_window()

    def click_on_element(self, exp_locator: str):
        CommonWaitings.wait_element_until_clickable(self, exp_locator, Constants.TIME_OUT_3S)
        self.driver.find_element(By.XPATH, exp_locator).click()
        print(f"Clicked on the element: {exp_locator}.")

    def send_key_to_element(self, exp_locator: str, exp_message: str):
        CommonWaitings.wait_element_until_visible(self, exp_locator, Constants.TIME_OUT_3S)
        self.driver.find_element(By.XPATH, exp_locator).clear()
        self.driver.find_element(By.XPATH, exp_locator).send_keys(exp_message)
        print(f"Provided {exp_message} into the element.")

    def get_text_from_element(self, exp_locator: str) -> str:
        CommonWaitings.wait_element_until_visible(self, exp_locator, Constants.TIME_OUT_3S)
        return self.driver.find_element(By.XPATH, exp_locator).text

    def get_text_from_element_by_attribute(self, exp_locator: str, attribute_name: str) -> str:
        CommonWaitings.wait_element_until_visible(self, exp_locator, Constants.TIME_OUT_3S)
        return self.driver.find_element(By.XPATH, exp_locator).get_attribute(attribute_name)
