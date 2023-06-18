import pytest
from spo.spofrag_exe.abstract_test import test_init
from spo.spofrag_utilities.prop_reader_utils import ReadGlobalVar as reader
from spo.spofrag_common_handler.commonfrag_constant.constant import Constant as const
from spo.spofrag_epic.functionality.log_in_page import LogInPage as log_in_page
from spo.spofrag_common_handler.wait_handler import WaitHandler as waiter


class Test_Log_In:
    __base_url = reader.get_app_url() + const.LOG_IN_PATH
    __usr_email_or_username = reader.get_user_email_or_username()
    __usr_pwd = reader.get_user_password()
    __passed_stt = const.TC_PASSED_STT
    __failed_stt = const.TC_FAILED_STT
    __func = const.FUNC_LOG_IN

    """
        test case 001: log in successfully to website: 
            - with spot-on credentials
            - leave remember me toggle unchecked 
    """

    def test_log_in_001(self, test_init):
        """
            if we log in to system from an automated script and driver is generated from
            selenium webdriver -> it also generates a robotic IP address leading to
            be banned by some security-enhanced websites, we may need to recaptcha to
            bypass this process. However, we do not need to repel the robot-recognized process
        """
        # fields declaration goes here
        tc_id: str = "001"
        self.driver_factory = test_init
        self.driver_factory.get(self.__base_url)

        # log in to spotify
        log_in_page.log_in(self, self.__usr_email_or_username, self.__usr_pwd, False)
        # waiter.force_wait(self, 100000000)
        # verify
