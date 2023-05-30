import contextlib
import time

import selenium.webdriver.support
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.ui import WebDriverWait


class CommonWaitings:

    def __init__(self, driver):
        self.driver = driver

    # second
    def sleep(self, time_out: int):
        time.sleep(time_out)

    def wait_element_until_visible(self, exp_locator: str, time_out: int) -> object:
        WebDriverWait(self.driver, time_out).until(
            selenium.webdriver.support.expected_conditions.visibility_of_element_located((By.XPATH, exp_locator)))

    def wait_element_until_clickable(self, exp_locator: str, time_out: int):
        WebDriverWait(self.driver, time_out).until(
            selenium.webdriver.support.expected_conditions.element_to_be_clickable((By.XPATH, exp_locator)))

    def wait_element_until_selected(self, exp_locator: str, time_out: int):
        WebDriverWait(self.driver, time_out).until(
            selenium.webdriver.support.expected_conditions.element_to_be_selected(self.driver.find_element(By.XPATH, exp_locator)))

    def wait_element_until_invisible(self, exp_locator: str, time_out: int):
        WebDriverWait(self.driver, time_out).until(
            selenium.webdriver.support.expected_conditions.invisibility_of_element(self.driver.find_element(By.XPATH, exp_locator)))

    @contextlib.contextmanager
    def wait_for_page_load(self, time_out: int) -> object:
        print("Waiting for page to load at {}.".format(self.driver.current_url))
        old_page = self.find_element_by_tag_name("html")
        yield
        WebDriverWait(self, time_out).until(staleness_of(old_page))
