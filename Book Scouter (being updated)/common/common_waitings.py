import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class CommonWaitings:

    def __init__(self, driver):
        self.driver = driver

    def sleep(self, time_out: int):
        time.sleep(time_out)

    def wait_element_until_visible(self, exp_locator: str, time_out: int) -> object:
        WebDriverWait(self.driver, time_out).until(
            expected_conditions.visibility_of_element_located((By.XPATH, exp_locator)))

    def wait_element_until_clickable(self, exp_locator: str, time_out: int):
        WebDriverWait(self.driver, time_out).until(
            expected_conditions.element_to_be_clickable((By.XPATH, exp_locator)))

    def wait_element_until_selected(self, exp_locator: str, time_out: int):
        WebDriverWait(self.driver, time_out).until(
            expected_conditions.element_to_be_selected(self.driver.find_element(By.XPATH, exp_locator)))

    def wait_element_until_invisible(self, exp_locator: str, time_out: int):
        WebDriverWait(self.driver, time_out).until(
            expected_conditions.invisibility_of_element(self.driver.find_element(By.XPATH, exp_locator)))
