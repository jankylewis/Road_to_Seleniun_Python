from common.common_ui_actions import CommonUIActions as common_ui_actions
from common.common_assertions import CommonAssertions as common_assertions
from common.common_waitings import CommonWaitings as common_waitings
from page_objects.log_in_page import LogInPage as log_in_page
from test_cases.abstract_test import setup
from page_objects.home_page import HomePage as home_page
from selenium.webdriver.common.by import By
from utilities.read_properties import ReadGlobalVariables as read_global_vars
from utilities.logger import LogGenerating
from page_objects.profile_page import ProfilePage as profile_page


class Test_Log_In:
    base_url = read_global_vars.get_application_url()
    user_email = read_global_vars.get_user_email()
    user_password = read_global_vars.get_user_password()
    wrong_user_password = str(0) + user_password

    log = LogGenerating.log_generating()

    """
    test case: log in unsuccessfully to website with spot-on credentials:
    -> improper user email
    -> improper user pwd
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
        self.driver.get(self.base_url)

        # take UI actions
        home_page.click_log_in_btn(self)
        log_in_page.set_user_email(self, self.user_email)
        log_in_page.set_user_password(self, self.user_password)
        log_in_page.click_log_in_btn(self)

        # check the presence of toast as an alert notification
        if home_page.verify_toast_is_visible(self):
            print("Logged in successfully toast was presented.")

            # navigate to profile page
            home_page.click_account_icon(self)
            home_page.click_account_ddi(self)

            # begin assertions
            if profile_page.verify_user_email(self, exp_user_email=self.user_email):
                print("Test case 001 was successfully!")
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
        self.driver.get(self.base_url)

        # take UI actions
        home_page.click_log_in_btn(self)
        log_in_page.set_user_email(self, self.user_email)
        log_in_page.set_user_password(self, "wrong" + self.user_password)
        log_in_page.click_log_in_btn(self)

        # begin assertions
        if log_in_page.verify_invalid_password_errmsg_is_presented(self):
            print("Test case 002 was successfully!")
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
        self.driver.get(self.base_url)

        # take UI actions
        home_page.click_log_in_btn(self)
        log_in_page.set_user_email(self, "wrong" + self.user_email)
        log_in_page.set_user_password(self, self.user_password)
        log_in_page.click_log_in_btn(self)

        # begin assertions
        if log_in_page.verify_bad_credentials_errmsg_is_presented(self):
            print("Test case 003 was successfully!")
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
        self.driver.get(self.base_url)

        # take UI actions
        home_page.click_log_in_btn(self)
        log_in_page.set_user_email(self, "wrong" + self.user_email)
        log_in_page.set_user_password(self, "wrong" + self.user_password)
        log_in_page.click_log_in_btn(self)

        # begin assertions
        if log_in_page.verify_bad_credentials_errmsg_is_presented(self):
            print("Test case 004 was successfully!")
            assert True
        else:
            print("Test case 004 was unsuccessfully!")
            assert False

        # tear down test cases
        self.driver.delete_all_cookies()
        self.log.warning("Deleted all cookies.")
        self.driver.quit()
        self.log.warning("Repelled driver.")
