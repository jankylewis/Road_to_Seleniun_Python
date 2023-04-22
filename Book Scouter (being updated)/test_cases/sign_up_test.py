from common.common_operator_helpers import CommonOperatorHelper as common_operations
from page_objects.home_page import HomePage as home_page
from page_objects.profile_page import ProfilePage as profile_page
from page_objects.sign_up_page import SignUpPage as sign_up
from utilities.read_properties import ReadGlobalVariables as read_global_vars

# must have to retrieve the setup method from fixture
from test_cases.abstract_test import setup


class Test_Sign_Up:
    __base_url = read_global_vars.get_application_url()
    __user_email = read_global_vars.get_user_email()
    __user_password = read_global_vars.get_user_password()
    __wrong_user_password = ""

    """
    test case: basic case to sign up successfully to website with spot-on credentials:
        + User checks on Newsletter checkbox by default
    """
    def test_sign_up_001(self, setup):
        print("\n*****/***** Sign up - Test case 001: *****/*****")

        # setup test case by declaring instances n pages
        self.driver = setup
        self.driver.get(self.__base_url)
        __exp_user_email = common_operations.randomizer(4, 1, 1) + self.__user_email

        # take UI actions
        home_page.click_sign_up_btn(self)
        sign_up.execute_register(self, exp_user_email=__exp_user_email, exp_user_pwd=self.__user_password)

        # verify the presence of toast notification
        if home_page.verify_toast(self):
            print("Logged in successfully toast was presented.")

            # navigate to profile page
            home_page.click_account_icon(self)
            home_page.click_account_ddi(self)

            # begin assertions
            if profile_page.verify_user_email(self, exp_user_email=__exp_user_email):
                print("User email matched.")
                print("Test case 001 was successful!")
                assert True
            else:
                print("Unfortunately, user email was not matched.")
                print("Test case 001 was unsuccessful!")
                assert False
        else:
            print("Successful logged-in toast made error.")
            print("Sorry, test case 001 was unsuccessful!")
            assert False

        # tear down test cases
        self.driver.delete_all_cookies()
        self.log.warning("Deleted all cookies.")
        self.driver.quit()
        self.log.warning("Repelled driver.")

        """
        test case: sign up successfully to website with spot-on credentials:
            + User unchecks on Newsletter checkbox
        """
    def test_sign_up_002(self, setup):
        print("\n*****/***** Sign up - Test case 002: *****/*****")

        # setup test case by declaring instances n pages
        self.driver = setup
        self.driver.get(self.__base_url)
        __exp_user_email = common_operations.randomizer(4, 1, 1) + self.__user_email

        # take UI actions
        home_page.click_sign_up_btn(self)
        sign_up.check_newsletter(self)
        sign_up.execute_register(self, exp_user_email=__exp_user_email, exp_user_pwd=self.__user_password)

        # verify the presence of toast notification
        if home_page.verify_toast(self):
            print("Logged in successfully toast was presented.")

            # navigate to profile page
            home_page.click_account_icon(self)
            home_page.click_account_ddi(self)

            # begin assertions
            if profile_page.verify_user_email(self, exp_user_email=__exp_user_email):
                print("User email matched.")
                print("Test case 002 was successful!")
                assert True
            else:
                print("Unfortunately, user email was not matched.")
                print("Test case 002 was unsuccessful!")
                assert False
        else:
            print("Successful logged-in toast made error.")
            print("Sorry, test case 002 was unsuccessful!")
            assert False

        # tear down test cases
        self.driver.delete_all_cookies()
        self.log.warning("Deleted all cookies.")
        self.driver.quit()
        self.log.warning("Repelled driver.")

    """
    test case: sign up successfully to website with spot-on credentials:
        + User checks on Newsletter checkbox by default
        + User checks on Become Pro checkbox:
            -> User does nothing on the register pro page
            -> User hits the Sign-up button
    """
    def test_sign_up_003(self, setup):
        print("\n*****/***** Sign up - Test case 003: *****/*****")

        # setup test case by declaring instances n pages
        self.driver = setup
        self.driver.get(self.__base_url)
        __exp_user_email = common_operations.randomizer(4, 1, 1) + self.__user_email

        # take UI actions
        home_page.click_sign_up_btn(self)
        sign_up.check_becoming_pro(self)
        sign_up.execute_register(self, exp_user_email=__exp_user_email, exp_user_pwd=self.__user_password)

        # navigate to register the credit card page

        # verify the presence of toast notification
        if home_page.verify_toast(self):
            print("Logged in successfully toast was presented.")
            sign_up.click_register_card(self)

            # begin assertions
            if sign_up.verify_register_pro_lbl(self):
                if sign_up.verify_cc_number_err_msg(self) \
                        and sign_up.verify_expired_date_err_msg(self) \
                        and sign_up.verify_cvc_err_msg(self):
                    print("Error messages were presented.")
                    print("Test case 002 was successful!")
                    assert True
            else:
                print("Sorry, test case 003 was unsuccessful!")
                assert False

            # tear down test cases
            self.driver.delete_all_cookies()
            self.log.warning("Deleted all cookies.")
            self.driver.quit()
            self.log.warning("Repelled driver.")

    """
    test case: sign up successfully to website with spot-on credentials:
        + User checks on Newsletter checkbox by default
    """
    def test_sign_up_004(self, setup):
        pass

    """
    test case: sign up unsuccessfully to website with improper credentials:
    -> User's email existed
    """
    def test_sign_up_005(self, setup):
        pass

    """
    test case: sign up unsuccessfully to website with improper credentials:
        + User's inputted email was invalid 
        (deficiency of @ sign, exceeding char limits, special char, ...)
        + User provides correct pwd
    """
    def test_sign_up_006(self, setup):
        print("\n*****/***** Sign up - Test case 006: *****/*****")

        # setup test case by declaring instances n pages
        self.driver = setup
        self.driver.get(self.__base_url)
        __exp_user_email = common_operations.randomizer(4, 1, 1)

        # take UI actions
        home_page.click_sign_up_btn(self)
        sign_up.set_user_email(self, __exp_user_email)
        sign_up.set_user_password(self, self.__user_password)

        # begin assertions
        if sign_up.verify_invalid_email_err_msg(self):
            print("Error message found.")
            print("Test case 006 was successful.")
            assert True
        else:
            print("Test case 006 was unsuccessful.")
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
        print("\n*****/***** Sign up - Test case 007: *****/*****")

        # setup test case by declaring instances n pages
        self.driver = setup
        self.driver.get(self.__base_url)
        __exp_user_pwd = common_operations.randomizer(1, 1, 1)

        # take UI actions
        home_page.click_sign_up_btn(self)
        sign_up.set_user_password(self, exp_user_pwd=__exp_user_pwd)
        sign_up.click_sign_up_btn(self)

        # begin assertions
        if sign_up.verify_invalid_pwd_err_msg(self) and sign_up.verify_input_email_err_msg(self):
            print("Error messages found.")
            print("Test case 007 was successful.")
            assert True
        else:
            print("Test case 007 was unsuccessful.")
            assert False

        # tear down test cases
        self.driver.delete_all_cookies()
        self.print("Deleted all cookies.")
        self.driver.quit()
        self.print("Repelled driver.")
