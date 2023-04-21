from selenium.webdriver.common.by import By
from locators.recaptcha_page import RecaptchaPage as recaptcha_page


class RecaptchaPage:
    CHK_RECAPTCHA = recaptcha_page.CHK_RECAPTCHA
    LBL_IP_ADDRESS = recaptcha_page.LBL_IP_ADDRESS
    HPL_CONTACT_SUPPORT = recaptcha_page.HPL_CONTACT_SUPPORT
    LBL_HUMAN_TITLE = recaptcha_page.LBL_HUMAN_TITLE

    def __init__(self, driver):
        self.driver = driver

    def click_on_recaptcha_checkbox(self):
        self.driver.find_element(By.XPATH, self.CHK_RECAPTCHA).click()

    def click_on_contact_support_hyperlink(self):
        self.driver.find_element(By.XPATH, self.HPL_CONTACT_SUPPORT).click()

    # have to assert human title and user's (attacker's) ip address
