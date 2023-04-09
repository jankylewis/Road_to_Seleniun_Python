from page_objects.login_page import LogInPage as log_in_page
from test_cases.config_test import setup
from page_objects.home_page import HomePage as home_page
from page_objects.recaptcha_page import RecaptchaPage as recaptcha_page
import time


class Test_Login:
    base_url = "https://www.nytimes.com/"
    log_in_url = "https://myaccount.nytimes.com/auth/login"
    user_email = "nick02092k@gmail.com"
    user_pwd = "tqvinh02092000"
    home_page_title = "The New York Times - Breaking News, US News, World News and Videos"

    # setup is imported from config_test
    # def test_001_home_page_title(self, setup):
    #     print("Start test case 001 of login.")
    #     self.driver = setup
    #     self.driver.get(self.base_url)
    #     # get text of home page title
    #     actual_title = self.driver.title
    #     # repel driver after completing purposes
    #     self.driver.close()
    #     # verify home page title
    #     if actual_title == self.home_page_title:
    #         print("Home page title matched expected title.")
    #         assert True
    #     else:
    #         print("Home page title did not match expected title.")
    #         assert False

    # setup is imported from config_test
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.log_in_url)
        time.sleep(50000)
        """ 
        if we login from an automated script and driver is generated from 
        selenium webdriver -> it also generates a robotic IP address leading to
        be banned by some security-enhanced websites, we may need to recaptcha to 
        bypass this process
        """
        self.log_in = log_in_page(self.driver)
        self.log_in.set_user_email(self.user_email)
        self.log_in.set_user_password(self.user_pwd)
        self.log_in.click_on_login_btn()
