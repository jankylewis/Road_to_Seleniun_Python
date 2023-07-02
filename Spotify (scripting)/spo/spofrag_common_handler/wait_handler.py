import time

from selenium.webdriver.support.ui import WebDriverWait as waiter
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.expected_conditions import staleness_of
from contextlib import contextmanager
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from spo.spofrag_common_handler.commonfrag_constant.constant import Constant as const
from selenium.common.exceptions import NoSuchElementException


class WaitHandler:

    def force_wait(self, time_out: float) -> None:

        # by seconds
        time.sleep(time_out)

    def wait_element_until_visible(self, exp_element: WebElement, time_out: int = const.TIME_OUT_3S,
                                   is_long_wait: bool = False) -> WebElement:
        """

        :rtype: WebElement
        """
        if is_long_wait:
            retry: int = 0
            while retry <= 5:
                try:
                    if waiter(self, time_out).until(ec.visibility_of_element_located(exp_element)):
                        return waiter(self, time_out).until(ec.visibility_of_element_located(exp_element))
                except NoSuchElementException as exception:

                    # one more infor
                    retry += 1

        else:

            # return element if not using long wait
            return waiter(self, time_out).until(ec.visibility_of_element_located(exp_element))

    def wait_element_until_clickable(self, exp_element: WebElement, time_out: int = const.TIME_OUT_5S) -> WebElement:
        """

        :param time_out:
        :type exp_element: WebElement
        """
        return waiter(self, time_out).until(ec.element_to_be_clickable(exp_element))

    @contextmanager
    def wait_for_page_fully_loaded(self, time_out=const.MAX_TIME_OUT) -> object:
        previous_page = self.find_element(By.TAG_NAME, 'html')
        yield
        waiter(self, time_out).until(staleness_of(previous_page))
