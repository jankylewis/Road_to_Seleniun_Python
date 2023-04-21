from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://bookscouter.com/")
time.sleep(1)
# driver.find_element(By.XPATH, "//button[@name = 'Sign Up']").click()
# time.sleep(1)
# driver.find_element(By.XPATH, "//input[@name = 'email']").send_keys("mathewryan001fances@gmail.com")
# time.sleep(1)
# driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys("12345678@Aa")
# time.sleep(1)
# driver.find_element(By.XPATH, "//button[@name = 'Sign Up' and @type = 'submit']").click()
# time.sleep(15)

driver.find_element(By.XPATH, "//button[@name = 'Log In']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@name = 'email']").send_keys("mathewryan001fances@gmail.com")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys("12345678@Aa")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@name = 'Login' and @type = 'submit']").click()
time.sleep(4)
driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Search')]").send_keys("1")
time.sleep(1)
driver.find_element(By.XPATH, "//button[@name = 'scout']").click()
time.sleep(4)
