from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import *
import time
import json
from essential_generators import DocumentGenerator
from spo.spofrag_utilities.test_utils.logs import Logging

class Test:
    num: int = None


def a():
    new_num: int = Test.num
    new_num = 2
    Test.num = new_num
    return Test.num


# driver = webdriver.Chrome()
# driver.get("https://www.google.com/")
#
# element: WebElement = By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]"
#
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located(element)
#     )
#
#     element.click()
# finally:
#     time.sleep(2)
#     driver.quit()

check: str = "false"


# print(type(json.loads(check.lower())))
# print(json.loads(check.lower()))


# def get_user_dob() -> str:
#     return (DocumentGenerator().gen_word())


# print(a())
# print(Test.num)

class TestSomething:
    pass
    # def setup(self, method):
    #     print("\n\nabcd%s:%s" % (type(self).__name__, method.__name__) + "\n\n")
    #
    # def teardown(self, method):
    #     print("tear")

    # def setup(self, method):
    #     class_name: str = type(self).__name__
    #     print("\nCLASS NAME: " + class_name)
    #
    #     method_name: str = method.__name__
    #     print("METHOD NAME: " + method_name)
    #
    # def test_the_power(self):
    #     assert True
    #
    # def test_something_else(self):
    #     assert True

x = Logging()
x.log_infor()


