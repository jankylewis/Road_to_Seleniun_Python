from locators.onboarding_experience import Onboarding as onboard
from selenium.webdriver.common.by import By


class LogInPage:
    TXT_EMAIL = onboard.TXT_USER_EMAIL
    TXT_PASSWORD = onboard.TXT_USER_PASSWORD
    BTN_LOG_IN = onboard.BTN_LOG_IN

    def __init__(self, driver):
        self.driver = driver

    def set_user_email(self, user_email):
        self.driver.find_element(By.XPATH, self.TXT_EMAIL).clear()
        self.driver.find_element(By.XPATH, self.TXT_EMAIL).send_keys(user_email)

    def set_user_password(self, user_pwd):
        self.driver.find_element(By.XPATH, self.TXT_EMAIL).clear()
        self.driver.find_element(By.XPATH, self.TXT_PASSWORD).send_keys(user_pwd)

    def click_on_log_in_btn(self):
        self.driver.find_element(By.XPATH, self.BTN_LOG_IN).click()
