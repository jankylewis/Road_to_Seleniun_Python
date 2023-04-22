from page_objects.home_page import HomePage as home_page
from page_objects.log_in_page import LogInPage as log_in_page
from page_objects.profile_page import ProfilePage as profile_page
from utilities.logger import LogGenerating
from utilities.read_properties import ReadGlobalVariables as read_global_vars
from common.common_operator_helpers import CommonOperatorHelper as operations
from test_cases.abstract_test import setup


class Test_Log_In:
    __base_url = read_global_vars.get_application_url()
    __user_email = read_global_vars.get_user_email()
    __user_password = read_global_vars.get_user_password()
    __wrong_user_password = str(0) + __user_password

    log = LogGenerating.log_generating()

    """
    test case: log in successfully to website with spot-on credentials:
    """

    def test_log_in_001(self, setup):
        """
        if we login from an automated script and driver is generated from
        selenium webdriver -> it also generates a robotic IP address leading to
        be banned by some security-enhanced websites, we may need to recaptcha to
        bypass this process. However, we do not need to repel the robot-recognized process
        """
        # setup test case by declaring instances n pages
        print("*****/***** Log in - Test case 001: *****/*****")
        self.driver = setup
        self.driver.get(self.__base_url)

        # take UI actions
        home_page.click_log_in_btn(self)
        log_in_page.set_user_email(self, self.__user_email)
        log_in_page.set_user_password(self, self.__user_password)
        log_in_page.click_log_in_btn(self)

        # check the presence of toast as an alert notification
        if home_page.verify_toast(self):
            print("Logged in successfully toast was presented.")

            # navigate to profile page
            home_page.click_account_icon(self)
            home_page.click_account_ddi(self)

            # begin assertions
            if profile_page.verify_user_email(self, exp_user_email=self.__user_email):
                print("Test case 001 was successful!")
                assert True
            else:
                print("Test case 001 was unsuccessfully!")
        else:
            print("Logged in successfully toast was not presented.")
            print("Test case 001 was unsuccessfully!")
            assert False
            exit()

        # tear down test cases
        self.driver.delete_all_cookies()
        self.log.warning("Deleted all cookies.")
        self.driver.quit()
        self.log.warning("Repelled driver.")

    """
    test case: log in unsuccessfully to website with incorrect password:
    -> correct user email
    -> improper user pwd
    """

    def test_log_in_002(self, setup):
        # setup test case by declaring instances n pages
        print("*****/***** Log in - Test case 002: *****/*****")
        self.driver = setup
        self.driver.get(self.__base_url)

        # take UI actions
        home_page.click_log_in_btn(self)
        log_in_page.set_user_email(self, self.__user_email)
        log_in_page.set_user_password(self, "wrong" + self.__user_password)
        log_in_page.click_log_in_btn(self)

        # begin assertions
        if log_in_page.verify_invalid_password_toast_is_presented(self):
            print("Test case 002 was successful!")
            assert True
        else:
            print("Test case 002 was unsuccessfully!")
            assert False

        # tear down test cases
        self.driver.delete_all_cookies()
        self.log.warning("Deleted all cookies.")
        self.driver.quit()
        self.log.warning("Repelled driver.")

    """
    test case: log in unsuccessfully to website with bad credentials:
    -> improper user email
    -> correct user pwd
    """

    def test_log_in_003(self, setup):
        # setup test case by declaring instances n pages
        print("*****/***** Log in - Test case 003: *****/*****")
        self.driver = setup
        self.driver.get(self.__base_url)

        # take UI actions
        home_page.click_log_in_btn(self)
        log_in_page.set_user_email(self, "wrong" + self.__user_email)
        log_in_page.set_user_password(self, self.__user_password)
        log_in_page.click_log_in_btn(self)

        # begin assertions
        if log_in_page.verify_bad_credentials_toast_is_presented(self):
            print("Test case 003 was successful!")
            assert True
        else:
            print("Test case 003 was unsuccessfully!")
            assert False

        # tear down test cases
        self.driver.delete_all_cookies()
        self.log.warning("Deleted all cookies.")
        self.driver.quit()
        self.log.warning("Repelled driver.")

    """
    test case: log in unsuccessfully to website with bad credentials:
    -> improper user email
    -> improper user pwd
    """

    def test_log_in_004(self, setup):
        # setup test case by declaring instances n pages
        print("*****/***** Log in - Test case 004: *****/*****")
        self.driver = setup
        self.driver.get(self.__base_url)

        # take UI actions
        home_page.click_log_in_btn(self)
        log_in_page.set_user_email(self, "wrong" + self.__user_email)
        log_in_page.set_user_password(self, "wrong" + self.__user_password)
        log_in_page.click_log_in_btn(self)

        # begin assertions
        if log_in_page.verify_bad_credentials_toast_is_presented(self):
            print("Test case 004 was successful!")
            assert True
        else:
            print("Test case 004 was unsuccessfully!")
            assert False

        # tear down test cases
        self.driver.delete_all_cookies()
        self.log.warning("Deleted all cookies.")
        self.driver.quit()
        self.log.warning("Repelled driver.")

    """
    test case: log in successfully to website with correct credentials:
    -> User navigates from sign-up page to log-in page
    """

    def test_log_in_005(self, setup):
        pass

    """
    test case: log in successfully to website with improper credentials:
        + User does nothing on log-in page
        + User hits log-in button
    """

    def test_log_in_006(self, setup):
        # setup test case by declaring instances n pages
        print("*****/***** Log in - Test case 006: *****/*****")
        self.driver = setup
        self.driver.get(self.__base_url)

        # take UI actions
        home_page.click_log_in_btn(self)

        # begin assertions
        if log_in_page.verify_input_email_err_msg(self) \
                and log_in_page.verify_input_pwd_err_msg(self):
            print("Test case 006 was successful!")
            assert True
        else:
            print("Sorry, test case 006 was unsuccessful!")
            assert False

        # tear down test cases
        self.driver.delete_all_cookies()
        self.log.warning("Deleted all cookies.")
        self.driver.quit()
        self.log.warning("Repelled driver.")


"""
 test case: log in successfully to website with improper credentials:
     + User provides an invalid format of email address
     + User hits log-in button
 """


def test_log_in_007(self, setup):
    # setup test case by declaring instances n pages
    print("*****/***** Log in - Test case 007: *****/*****")
    self.driver = setup
    self.driver.get(self.__base_url)
    __rand_str: str = operations.randomizer(3, 1, 1)

    # take UI actions
    log_in_page.set_user_email(self, __rand_str)
    home_page.click_log_in_btn(self)

    # begin assertions
    if log_in_page.verify_invalid_email_err_msg(self) \
            and log_in_page.verify_input_pwd_err_msg(self):
        print("Test case 007 was successful!")
        assert True
    else:
        print("Sorry, test case 007 was unsuccessful!")
        assert False

    # tear down test cases
    self.driver.delete_all_cookies()
    self.log.warning("Deleted all cookies.")
    self.driver.quit()
    self.log.warning("Repelled driver.")
