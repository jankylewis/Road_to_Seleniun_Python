import pytest
from selenium import webdriver

from common.common_ui_actions import CommonUIActions as common_ui_actions


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    # LogGenerating.log_generating().info("*****/***** Chrome driver was initialized *****/*****")
    print("\n\n*****/***** Chrome driver was initialized *****/*****")
    common_ui_actions.maximize_popup(driver)
    print("Popped up screen was maximized.")
    return driver
