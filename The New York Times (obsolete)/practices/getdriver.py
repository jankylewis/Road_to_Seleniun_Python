from selenium import webdriver
import unittest


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.python.org")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
