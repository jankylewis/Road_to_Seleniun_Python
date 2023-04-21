from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    print("\nChrome driver was initialized.")
    return driver



