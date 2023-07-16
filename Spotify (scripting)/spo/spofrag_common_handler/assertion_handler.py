from spo.spofrag_common_handler.commonfrag_constant.constant import Constant as const
from spo.spofrag_common_handler.wait_handler import WaitHandler as waiter
from selenium.webdriver.remote.webelement import *
from selenium.webdriver.common.by import By
import pandas as pd
from pandas import Series, Timestamp
from spo.spofrag_utilities.test_utils.logs import Logging as log_utils


class AssertionHandler:
    driver_factory = None

    def __init__(self, driver_factory):
        self.driver_factory = driver_factory

    def verify_element_is_visible(self, exp_element: WebElement, time_out: int = const.TIME_OUT_3S,
                                  is_long_wait: bool = False) -> bool:
        exp_element = waiter.wait_element_until_visible(self, exp_element, time_out, is_long_wait)

        return exp_element.is_displayed()

    @staticmethod
    def handle_test_assertion(test_name: str, test_stt: str):
        if test_stt is const.TC_PASSED_STT:
            log_utils.log_test_stt(test_name=test_name,
                                   test_stt=const.TC_PASSED_STT)
            assert True
        elif test_stt is const.TC_FAILED_STT:
            log_utils.log_test_stt(test_name=test_name,
                                   test_stt=const.TC_FAILED_STT)
            assert False
        else:
            raise AssertionError

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
            print(
                f"Expected {exp_str} to contain {str_to_be_contained} but found False"
            )
            return False

    def is_displayed(self, exp_element: By) -> bool:
        exp_element = waiter.wait_element_until_visible(
            self.driver_factory, exp_element, const.TIME_OUT_3S
        )
        return exp_element.is_selected()

    @staticmethod
    def verify_datetime(exp_date: str, act_date: str) -> bool:
        is_checked: bool = False
        act_form: Series | Timestamp | Timestamp = pd.to_datetime(act_date)
        exp_form: Series | Timestamp | Timestamp = pd.to_datetime(exp_date)

        if (
                act_form.day == exp_form.day
                and act_form.month == exp_form.month
                and act_form.year == exp_form.year
        ):
            print(f"{exp_date} was equal to {act_date}")
            is_checked = True
        else:
            print(f"Expected {exp_date} to be equal to {act_date} but found False")
            is_checked = False

        return is_checked

    #     __log = log_utils()
    #
    #     # expectation is receiving log_type as an enum value
    #     @classmethod
    #     def log_af_assertions(cls,
    #                           test_stt: str,
    #                           test_name: str = None,
    #                           log_type: str = msg_const.get_informative_type(),
    #                           log_msg: str = None):
    #         is_passed: bool = False
    #
    #         # checking log_type
    #         if log_type is msg_const.get_informative_type():
    #             print("\n")
    #             print("1")
    #             log = log_utils()
    #             print("LOG INFOR: " + str(log.log_infor(log_msg=f"{test_name} -> {log_msg}")))
    #             print("2")
    #         elif log_type is msg_const.get_warning_type():
    #             cls.__log.log_warning(log_msg)
    #         elif log_type is msg_const.get_debug_type():
    #             cls.__log.log_debug(log_msg)
    #         elif log_type is msg_const.get_error_type():
    #             cls.__log.log_error(log_msg)
    #         else:
    #             cls.__log.log_critical(log_msg)
    #
    #         # assertions
    #         if test_stt is not const.TC_PASSED_STT:
    #             assert is_passed
    #         else:
    #             assert not is_passed
