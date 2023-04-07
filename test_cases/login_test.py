from page_objects.login_page import Login
from test_cases.config_test import setup


class Test_Login_001:
    base_url = "https://www.nytimes.com/"
    user_email = "nick02092k@gmail.com"
    user_pwd = "tqvinh02092000"

    # setup is imported from config_test
    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title
        # repel driver after completing purposes
        self.driver.close()
        print(actual_title)
        assert True

    # setup is imported from config_test
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.login = Login(self.driver)
        self.login.set_user_email(self.user_email)
        self.login.set_user_password(self.user_pwd)
        self.login.click_on_login_btn()
