import time

from spo.spofrag_exe.abstract_test import test_flow
from spo.spofrag_exe.abstract_test import DriverManager as driver_manager
from spo.spofrag_utilities.prop_reader_utils import ReadGlobalVar as reader
from spo.spofrag_common_handler.commonfrag_constant.constant import Constant as const
from spo.spofrag_epic.functionality.log_in_page import LogInPage as log_in_page
from spo.spofrag_epic.model.user_information_model import UserInformationModel as user_model
from spo.spofrag_epic.functionality.account_information_page import AccountInformationPage as account_page


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

    def test_log_in_001(self, test_flow):
        """
        if we log in to system from an automated script and driver is generated from
        selenium webdriver -> it also generates a robotic IP address leading to
        be banned by some security-enhanced websites, we may need to recaptcha to
        bypass this process. However, we do not need to repel the robot-recognized process
        """
        # fields declaration goes here
        tc_id: str = "001"
        self.driver_factory = driver_manager.get_driver_factory()
        self.driver_factory.get(self.__base_url)

        # produce model
        __user_model_produced: user_model = self.produce_user_model

        # log in to spotify
        log_in_page.log_in(self, self.__usr_email_or_username, self.__usr_pwd, False)

        # verification goes here
        if account_page.verify_account_page_presented(self, __user_model_produced):
            assert True
        else:
            assert False

        time.sleep(10000000)

    @property
    def produce_user_model(self) -> user_model:

        return user_model(
            user_email_or_username=reader.get_user_email_or_username(),
            user_dob=reader.get_user_dob(),
            user_nation=reader.get_user_nation(),
        )
