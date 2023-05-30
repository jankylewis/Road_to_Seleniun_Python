from selenium.webdriver.common import keys
from common.common_waitings import CommonWaitings
from selenium.webdriver.common.by import By
from common.common_assertions import CommonAssertions
from common.constants import Constants

# press key associated with locators
from selenium.webdriver.common.keys import Keys

# press key without association with locators
from selenium.webdriver.common.action_chains import ActionChains as actions


class CommonUIActions:

    def __init__(self, driver):
        self.driver = driver

    def maximize_popup(self: object) -> None:
        """

        :rtype: object
        """
        self.maximize_window()

    # click on controls: checkbox, text, button, radio n some others
    def click_on_element(self, exp_locator: str):
        CommonWaitings.wait_element_until_clickable(self, exp_locator, Constants.TIME_OUT_3S)
        self.driver.find_element(By.XPATH, exp_locator).click()
        print(f"Clicked on the element: {exp_locator}.")

    def send_key_to_element(self, exp_locator: str, exp_message: str):
        CommonWaitings.wait_element_until_visible(self, exp_locator, Constants.TIME_OUT_3S)
        self.driver.find_element(By.XPATH, exp_locator).clear()
        self.driver.find_element(By.XPATH, exp_locator).send_keys(exp_message)
        print(f"Provided {exp_message} into the element.")

    def get_text_from_element(self, exp_locator: str) -> str:
        CommonWaitings.wait_element_until_visible(self, exp_locator, Constants.TIME_OUT_3S)
        return self.driver.find_element(By.XPATH, exp_locator).text

    def get_text_from_element_by_attribute(self, exp_locator: str, attribute_name: str) -> str:
        CommonWaitings.wait_element_until_visible(self, exp_locator, Constants.TIME_OUT_3S)
        return self.driver.find_element(By.XPATH, exp_locator).get_attribute(attribute_name)

    # key press associated with specific elements
    def press_key_by_element(self, exp_locator: str, key_received: str):
        CommonWaitings.wait_element_until_visible(self, exp_locator, Constants.TIME_OUT_3S)
        if CommonAssertions.verify_string_is_equal(Constants.KEY_ENTER, key_received):
            self.driver.find_element(By.XPATH, exp_locator).send_keys(Keys.ENTER)
            print("Pressed enter.")
        elif CommonAssertions.verify_string_is_equal(Constants.KEY_BACKSPACE, key_received):
            self.driver.find_element(By.XPATH, exp_locator).send_keys(Keys.BACKSPACE)
            print("Pressed backspace.")
        elif CommonAssertions.verify_string_is_equal(Constants.KEY_TAB, key_received):
            self.driver.find_element(By.XPATH, exp_locator).send_keys(Keys.TAB)
            print("Pressed tab.")
        elif CommonAssertions.verify_string_is_equal(Constants.KEY_SPACE, key_received):
            self.driver.find_element(By.XPATH, exp_locator).send_keys(Keys.SPACE)
            print("Pressed space.")
        elif CommonAssertions.verify_string_is_equal(Constants.KEY_PAGE_UP, key_received):
            self.driver.find_element(By.XPATH, exp_locator).send_keys(Keys.PAGE_UP)
            print("Pressed page up.")
        elif CommonAssertions.verify_string_is_equal(Constants.KEY_PAGE_DOWN, key_received):
            self.driver.find_element(By.XPATH, exp_locator).send_keys(Keys.PAGE_DOWN)
            print("Pressed page down.")
        elif CommonAssertions.verify_string_is_equal(Constants.KEY_F5, key_received):
            self.driver.find_element(By.XPATH, exp_locator).send_keys(Keys.F5)
            print("Pressed F5.")
        else:
            print("Your key was not valid.")

    # key press can be used without depending on specific elements
    # def action_enter(self, action_received: str):
    #     __actions = actions(self.driver)
    #     if CommonAssertions.verify_string_is_equal(Constants.KEY_ENTER, action_received):
    #         __actions.send_keys(self, keys.Keys.ENTER).perform(self)
    #         print("Performed pressing enter.")
