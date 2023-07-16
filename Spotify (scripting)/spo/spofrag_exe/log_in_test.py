import pytest
from selenium import webdriver
from spo.spofrag_exe.abstract_test import test_factory
from spo.spofrag_exe.abstract_test import driver_manager, AbstractTest
from spo.spofrag_utilities.prop_reader_utils import ReadGlobalVar as reader
from spo.spofrag_common_handler.commonfrag_constant.constant import Constant as const
from spo.spofrag_epic.functionality.log_in_page import LogInPage as log_in_page
from spo.spofrag_epic.model.user_information_model import UserInformationModel as user_model
from spo.spofrag_epic.functionality.account_information_page import AccountInformationPage as account_page
from spo.spofrag_common_handler.assertion_handler import AssertionHandler as verifier

"""
if we log in to system from an automated script and driver is generated from
selenium webdriver -> it also generates a robotic IP address leading to
be banned by some security-enhanced websites, we may need to recaptcha to
bypass this process. However, we do not need to repel the robot-recognized process
"""


class Test_Log_In(AbstractTest):
    driver_factory = None

    __base_url = reader.get_app_url() + const.LOG_IN_PATH
    __usr_email_or_username = reader.get_user_email_or_username()
    __usr_pwd = reader.get_user_password()

    __passed_stt = const.TC_PASSED_STT
    __failed_stt = const.TC_FAILED_STT
    __test_name: str

    """
        test case 001: log in successfully to website: 
            - with spot-on credentials
            - leave remember me toggle unchecked 
    """

    @pytest.mark.order(1)
    def test_log_in_001(self, test_factory: None):

        # fields declaration goes here
        __user_model_produced: user_model = self.produce_user_model()

        # log in to spotify
        log_in_page.log_in(self,
                           self.__usr_email_or_username,
                           self.__usr_pwd,
                           False)

        # log-in verification goes here
        if account_page.verify_account_page_presented(self,
                                                      __user_model_produced):
            verifier.handle_test_assertion(test_name=self.__test_name,
                                           test_stt=self.__passed_stt)
        else:
            verifier.handle_test_assertion(test_name=self.__test_name,
                                           test_stt=self.__failed_stt)

    @pytest.mark.order(2)
    def test_log_in_002(self, test_factory: None):

        # log in to spotify
        log_in_page.log_in(self,
                           self.__usr_email_or_username,
                           self.__usr_pwd + "wrong",
                           False)

        # log-in verification goes here
        if log_in_page.verify_log_in_unsuccessfully(self):
            verifier.handle_test_assertion(test_name=self.__test_name,
                                           test_stt=self.__passed_stt)
        else:
            verifier.handle_test_assertion(test_name=self.__test_name,
                                           test_stt=self.__failed_stt)

    @classmethod
    def produce_user_model(cls, exp_usr_model: user_model = None) -> user_model:

        if exp_usr_model is not None:
            return exp_usr_model
        else:
            return user_model(user_email_or_username=reader.get_user_email_or_username(),
                              user_dob=reader.get_user_dob(),
                              user_nation=reader.get_user_nation())

    @classmethod
    @pytest.mark.usefixtures("test_factory")
    def setup_method(cls, method) -> webdriver:

        test_address: str = f"{type(cls).__name__} -> {method.__name__}"
        cls.__test_name = test_address

        cls.driver_factory = driver_manager.get_driver_factory()
        cls.driver_factory.get(cls.__base_url)

        return cls.driver_factory

    # @classmethod
    # def teardown_method(cls, method):
    #     raise Exception
