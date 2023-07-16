import pytest

from selenium import webdriver
from spo.spofrag_utilities.test_utils.driver_manager import DriverManager as driver_manager
from spo.spofrag_utilities.test_utils.cookies_manager import CookiesManager as cookies_manager
from spo.spofrag_common_handler.commonfrag_constant.constant import Constant as const


@pytest.fixture(scope=const.FUNCTION_SCOPE, autouse=True)
def test_factory():
    general_setup()

    yield
    general_teardown()


def general_setup():
    __driver_produced = driver_manager.produce_driver()
    driver_manager.set_driver_factory(__driver_produced)
    driver_manager.driver_factory_used.maximize_window()


def general_teardown():
    __driver_produced = driver_manager.driver_factory_used
    if __driver_produced is not None:
        cookies_manager.delete_all_cookies(__driver_produced)
        __driver_produced.quit()


class AbstractTest:
    # driver using in test class
    driver_factory: webdriver
