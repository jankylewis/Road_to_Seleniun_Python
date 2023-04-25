import pytest

from common.common_operation_helpers import CommonOperatorHelper as common_ope
from common.constants import Constants as const
from page_objects.onboard_experience.home_page import HomePage as home_page
from page_objects.onboard_experience.profile_page import ProfilePage as profile_page
from page_objects.onboard_experience.sign_up_page import SignUpPage as sign_up
from utilities.read_properties import ReadGlobalVariables as read_global_vars
# must have to retrieve the setup method from fixture


@pytest.mark.usefixtures("setup")
class Test_Sign_Up:
    __base_url = read_global_vars.get_application_url()
    __user_email = read_global_vars.get_user_email()
    __user_password = read_global_vars.get_user_password()
    __wrong_user_password = ""
    __passed_stt: str = const.TC_PASSED_STATUS
    __failed_stt: str = const.TC_FAILED_STATUS
    __function_test: str = const.TC_SIGN_UP_FUNCTION

    """
    test case: basic case to sign up successfully to website with spot-on credentials:
        + User checks on Newsletter checkbox by default
    """

    def test_sign_up_001(self, setup):
        __tc_id: str = "001"
        print(f"\n*****/***** {self.__function_test} - Test case {__tc_id}: *****/*****\n")

        # setup test case by declaring instances n pages
        self.driver = setup
        self.driver.get(self.__base_url)
        __exp_user_email = common_ope.randomizer(4, 1, 1) + self.__user_email

        # take UI actions
        home_page.click_sign_up_btn(self)
        sign_up.execute_register(self, exp_user_email=__exp_user_email, exp_user_pwd=self.__user_password)

        # verify the presence of toast notification
        if home_page.verify_toast(self):

            # navigate to profile page
            home_page.click_account_icon(self)
            home_page.click_account_ddi(self)

            # begin assertions
            if profile_page.verify_user_email(self, exp_user_email=__exp_user_email):
                common_ope.log_test_case_status(__tc_id, self.__passed_stt)
                assert True
            else:
                common_ope.log_test_case_status(__tc_id, self.__failed_stt)
                assert False
        else:
            common_ope.log_test_case_status(__tc_id, self.__failed_stt)
            assert False

        # tear down test cases
        self.driver.delete_all_cookies()
        print("Deleted all cookies.")
        self.driver.quit()
        print("Repelled driver.")

        """
        test case: sign up successfully to website with spot-on credentials:
            + User unchecks on Newsletter checkbox
        """

    def test_sign_up_002(self, setup):
        __tc_id: str = "002"
        print(f"\n*****/***** {self.__function_test} - Test case {__tc_id}: *****/*****\n")

        # setup test case by declaring instances n pages
        self.driver = setup
        self.driver.get(self.__base_url)
        __exp_user_email = common_ope.randomizer(4, 1, 1) + self.__user_email

        # take UI actions
        home_page.click_sign_up_btn(self)
        sign_up.check_newsletter(self)
        sign_up.execute_register(self, exp_user_email=__exp_user_email, exp_user_pwd=self.__user_password)

        # verify the presence of toast notification
        if home_page.verify_toast(self):

            # navigate to profile page
            home_page.click_account_icon(self)
            home_page.click_account_ddi(self)

            # begin assertions
            if profile_page.verify_user_email(self, exp_user_email=__exp_user_email):
                common_ope.log_test_case_status(__tc_id, self.__passed_stt)
                assert True
            else:
                common_ope.log_test_case_status(__tc_id, self.__failed_stt)
                assert False
        else:
            common_ope.log_test_case_status(__tc_id, self.__failed_stt)
            assert False

        # tear down test cases
        self.driver.delete_all_cookies()
        print("Deleted all cookies.")
        self.driver.quit()
        print("Repelled driver.")

    """
    test case: sign up successfully to website with spot-on credentials:
        + User checks on Newsletter checkbox by default
        + User checks on Become Pro checkbox:
            -> User does nothing on the register pro page
            -> User hits the Sign-up button
    """

    def test_sign_up_003(self, setup):
        __tc_id: str = "003"
        print(f"\n*****/***** {self.__function_test} - Test case {__tc_id}: *****/*****\n")

        # setup test case by declaring instances n pages
        self.driver = setup
        self.driver.get(self.__base_url)
        __exp_user_email = common_ope.randomizer(4, 1, 1) + self.__user_email

        # take UI actions
        home_page.click_sign_up_btn(self)
        sign_up.check_becoming_pro(self)
        sign_up.execute_register(self, exp_user_email=__exp_user_email, exp_user_pwd=self.__user_password)

        # navigate to register the credit card page

        # verify the presence of toast notification
        if home_page.verify_toast(self):
            sign_up.click_register_card(self)

            # begin assertions
            if sign_up.verify_register_pro_lbl(self):
                if sign_up.verify_cc_number_err_msg(self) \
                        and sign_up.verify_expired_date_err_msg(self) \
                        and sign_up.verify_cvc_err_msg(self):
                    common_ope.log_test_case_status(__tc_id, self.__passed_stt)
                    assert True
            else:
                common_ope.log_test_case_status(__tc_id, self.__failed_stt)
                assert False

            # tear down test cases
            self.driver.delete_all_cookies()
            print("Deleted all cookies.")
            self.driver.quit()
            print("Repelled driver.")

    """
    test case: sign up successfully to website with spot-on credentials:
        + User unchecks on Newsletter checkbox
        + User checks on Become Pro checkbox:
            -> User does nothing on the register pro page
            -> User hits the Sign-up button
    """

    def test_sign_up_004(self, setup):
        __tc_id: str = "004"
        print(f"\n*****/***** {self.__function_test} - Test case {__tc_id}: *****/*****\n")

        # setup test case by declaring instances n pages
        self.driver = setup
        self.driver.get(self.__base_url)
        __exp_user_email = common_ope.randomizer(4, 1, 1) + self.__user_email

        # take UI actions
        home_page.click_sign_up_btn(self)
        sign_up.check_newsletter(self)
        sign_up.check_becoming_pro(self)
        sign_up.execute_register(self, exp_user_email=__exp_user_email, exp_user_pwd=self.__user_password)

        # navigate to register the credit card page

        # verify the presence of toast notification
        if home_page.verify_toast(self):
            sign_up.click_register_card(self)

            # begin assertions
            if sign_up.verify_register_pro_lbl(self):
                if sign_up.verify_cc_number_err_msg(self) \
                        and sign_up.verify_expired_date_err_msg(self) \
                        and sign_up.verify_cvc_err_msg(self):
                    common_ope.log_test_case_status(__tc_id, self.__passed_stt)
                    assert True
            else:
                common_ope.log_test_case_status(__tc_id, self.__failed_stt)
                assert False

            # tear down test cases
            self.driver.delete_all_cookies()
            print("Deleted all cookies.")
            self.driver.quit()
            print("Repelled driver.")

    """
    test case: sign up unsuccessfully to website with improper credentials:
        + User's email existed
    """

    def test_sign_up_005(self, setup):
        __tc_id: str = "005"
        print(f"\n*****/***** {self.__function_test} - Test case {__tc_id}: *****/*****\n")

        # setup test case by declaring instances n pages
        self.driver = setup
        self.driver.get(self.__base_url)
        __exp_existed_user_email = self.__user_email

        # take UI actions
        home_page.click_sign_up_btn(self)
        sign_up.check_newsletter(self)
        sign_up.check_becoming_pro(self)
        sign_up.execute_register(self, exp_user_email=__exp_existed_user_email, exp_user_pwd=self.__user_password)

        # assertions
        if sign_up.verify_existed_email_toast_presented(self):
            common_ope.log_test_case_status(__tc_id, self.__passed_stt)
            assert True
        else:
            common_ope.log_test_case_status(__tc_id, self.__failed_stt)
            assert False

        # tear down test cases
        self.driver.delete_all_cookies()
        print("Deleted all cookies.")
        self.driver.quit()
        print("Repelled driver.")

    """
    test case: sign up unsuccessfully to website with improper credentials:
        + User's inputted email was invalid 
        (deficiency of @ sign, exceeding char limits, special char, ...)
        + User provides correct pwd
    """

    def test_sign_up_006(self, setup):
        __tc_id: str = "006"
        print(f"\n*****/***** {self.__function_test} - Test case {__tc_id}: *****/*****\n")

        # setup test case by declaring instances n pages
        self.driver = setup
        self.driver.get(self.__base_url)
        __exp_user_email = common_ope.randomizer(4, 1, 1)

        # take UI actions
        home_page.click_sign_up_btn(self)
        sign_up.set_user_email(self, __exp_user_email)
        sign_up.set_user_password(self, self.__user_password)

        # begin assertions
        if sign_up.verify_invalid_email_err_msg(self):
            common_ope.log_test_case_status(__tc_id, self.__passed_stt)
            assert True
        else:
            common_ope.log_test_case_status(__tc_id, self.__failed_stt)
            assert False

        # tear down test cases
        self.driver.delete_all_cookies()
        print("Deleted all cookies.")
        self.driver.quit()
        print("Repelled driver.")

    """
    test case: sign up unsuccessfully to website with improper credentials:
        + User's inputted pwd was invalid (dissatisfied pwd standard of website)
        + User leaves blank to email field
    """

    def test_sign_up_007(self, setup):
        __tc_id: str = "007"
        print(f"\n*****/***** {self.__function_test} - Test case {__tc_id}: *****/*****\n")

        # setup test case by declaring instances n pages
        self.driver = setup
        self.driver.get(self.__base_url)
        __exp_user_pwd = common_ope.randomizer(1, 1, 1)

        # take UI actions
        home_page.click_sign_up_btn(self)
        sign_up.set_user_password(self, exp_user_pwd=__exp_user_pwd)
        sign_up.click_sign_up_btn(self)
        # waiter.sleep(self, 2)

        # begin assertions
        if sign_up.verify_invalid_pwd_err_msg(self):  # and sign_up.verify_input_email_err_msg(self):
            common_ope.log_test_case_status(__tc_id, self.__passed_stt)
            assert True
        else:
            common_ope.log_test_case_status(__tc_id, self.__failed_stt)
            assert False

        # tear down test cases
        self.driver.delete_all_cookies()
        print("Deleted all cookies.")
        self.driver.quit()
        print("Repelled driver.")
