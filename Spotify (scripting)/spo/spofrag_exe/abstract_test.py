import pytest

from spo.spofrag_utilities.test_utils.driver_manager import DriverManager
from spo.spofrag_utilities.test_utils.cookies_manager import CookiesManager


@pytest.fixture()
def test_factory():
    general_setup()

    yield
    general_teardown()


def general_setup():
    __driver_produced = DriverManager.produce_driver()
    DriverManager.set_driver_factory(__driver_produced)
    DriverManager.driver_factory_used.maximize_window()


def general_teardown():
    __driver_produced = DriverManager.driver_factory_used
    if __driver_produced is not None:
        CookiesManager.delete_all_cookies(__driver_produced)
        __driver_produced.quit()
