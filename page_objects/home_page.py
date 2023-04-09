from locators.home_page import HomePage as home_page
from selenium.webdriver.common.by import By


class HomePage:
    BTN_LOGIN = home_page.BTN_LOG_IN
    BTN_WEEKLY_SUBSCRIBE = home_page.BTN_WEEKLY_SUBSCRIBE
    BTN_MENU = home_page.BTN_MENU
    BTN_SEARCH = home_page.BTN_SEARCH
    BTN_GO = home_page.BTN_GO
    TXT_SEARCH = home_page.TXT_SEARCH

    def __init__(self, driver):
        self.driver = driver

    def click_on_log_in_btn(self):
        self.driver.find_element(By.XPATH, self.BTN_LOGIN).click()

    def click_on_weekly_subscribe_btn(self):
        self.driver.find_element(By.XPATH, self.BTN_WEEKLY_SUBSCRIBE).click()

    def click_on_menu_btn(self):
        self.driver.find_element(By.XPATH, self.BTN_MENU).click()

    def click_on_search_btn(self):
        self.driver.find_element(By.XPATH, self.BTN_SEARCH).click()

    def click_on_go_btn(self):
        self.driver.find_element(By.XPATH, self.BTN_GO).click()

    def set_search_key(self, search_key):
        self.driver.find_element(By.XPATH, self.TXT_SEARCH).clear()
        self.driver.find_element(By.XPATH, self.TXT_SEARCH).send_keys(search_key)
