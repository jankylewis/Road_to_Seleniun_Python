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


class Test_Sign_Up:
    base_url = read_global_vars.get_application_url()
    user_email = read_global_vars.get_user_email()
    user_password = read_global_vars.get_user_password()
    wrong_user_password = str(0) + user_password

    """
    test case: basic case to sign up successfully to website with spot-on credentials:
    """

    def test_sign_up_001(self, setup):
        pass

    """
    test case: sign up successfully to website with spot-on credentials:
    -> User checks on Newsletter checkbox
    """

    def test_sign_up_002(self, setup):
        pass

    """
    test case: sign up successfully to website with spot-on credentials:
    -> User checks on Become Pro checkbox
    """

    def test_sign_up_003(self, setup):
        pass

    """
    test case: sign up successfully to website with spot-on credentials:
    -> User checks on Newsletter checkbox
    -> User checks on Become Pro checkbox
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
    -> User's inputted email was invalid (deficiency of @ sign, exceeding char limits, special char, ...)
    """

    def test_sign_up_006(self, setup):
        pass

    """
    test case: sign up unsuccessfully to website with improper credentials:
    -> User's inputted pwd was invalid (dissatisfied pwd standard of website)
    """

    def test_sign_up_007(self, setup):
        pass
