import pytest
from selenium import webdriver

from common.common_ui_actions import CommonUIActions as common_ui_actions
from utilities.read_properties import ReadGlobalVariables as read_global_vars
from common.constants import Constants as const
from webdriver_manager.opera import OperaDriverManager


@pytest.fixture(autouse=True)
def setup():
    __browser = retrieve_browser()
    if const.CHROME_BR == __browser:
        driver = webdriver.Chrome()
        print(f"\n\n*****/***** {__browser.capitalize()} driver was initialized *****/*****")
    elif const.FIREFOX_BR == __browser:
        driver = webdriver.Firefox()
        print(f"\n\n*****/***** {__browser.capitalize()} driver was initialized *****/*****")
    elif const.IE_BR == __browser:
        driver = webdriver.Ie()
        print(f"\n\n*****/***** {__browser.capitalize()} driver was initialized *****/*****")
    elif const.EDGE_BR == __browser:
        driver = webdriver.Edge()
        print(f"\n\n*****/***** {__browser.capitalize()} driver was initialized *****/*****")
    elif const.OPERA_BR == __browser:
        # customize opera driver to trigger
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        print(f"\n\n*****/***** {__browser.capitalize()} driver was initialized *****/*****")
    elif const.SAFARI_BR == __browser:
        driver = webdriver.Safari()
        print(f"\n\n*****/***** {__browser.capitalize()} driver was initialized *****/*****")
    elif const.BRAVE_BR == __browser:
        # custom brave br utilizing desired capabilities
        print(f"\n\n*****/***** {__browser.capitalize()} driver was initialized *****/*****")
    else:
        print(
            f"\n\n*****/***** Your browser name was not valid, please re-execute script and provide another valid browser name *****/*****")
    common_ui_actions.maximize_popup(driver)
    print("\n*****/***** Popped up screen was maximized *****/*****")
    return driver


def retrieve_browser() -> str:
    # get browser from global var file
    __browser_type = read_global_vars.get_browser_type()
    if const.CHROME_BR == __browser_type:
        return const.CHROME_BR
    elif const.FIREFOX_BR == __browser_type:
        return const.FIREFOX_BR
    elif const.IE == __browser_type:
        return const.IE_BR
    elif const.EDGE_BR == __browser_type:
        return const.EDGE_BR
    elif const.SAFARI_BR == __browser_type:
        return const.SAFARI_BR
    elif const.OPERA_BR == __browser_type:
        return const.OPERA_BR
    elif const.BRAVE_BR == __browser_type:
        return const.BRAVE_BR


""" these lines of code are kept for reference purposes only -> in order to explore triggering browser type to run by CLI (hook)

@pytest.fixture(autouse=True)
def setup(browser):
def setup(browser):
    if str(browser).lower() == "chrome":
        driver = webdriver.Chrome()
        print(f"\n\n*****/***** {str(browser).capitalize()} driver was initialized *****/*****")
    elif str(browser).lower() == "firefox" or str(browser).lower() == "gecko":
        driver = webdriver.Firefox()
        print(f"\n\n*****/***** {str(browser).capitalize()} driver was initialized *****/*****")
    elif str(browser).lower() == "ie":
        driver = webdriver.Ie()
        print(f"\n\n*****/***** {str(browser).capitalize()} driver was initialized *****/*****")
    elif str(browser).lower() == "edge":
        driver = webdriver.Edge()
        print(f"\n\n*****/***** {str(browser).capitalize()} driver was initialized *****/*****")
    elif str(browser).lower() == "opera":
        # customize opera driver to trigger
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        print(f"\n\n*****/***** {str(browser).capitalize()} driver was initialized *****/*****")
    elif str(browser).lower() == "safari":
        driver = webdriver.Safari()
        print(f"\n\n*****/***** {str(browser).capitalize()} driver was initialized *****/*****")
    elif str(browser).lower() == "brave":
        # custom brave br utilizing desired capabilities
        print(f"\n\n*****/***** {str(browser).capitalize()} driver was initialized *****/*****")
    else:
        print(
            f"\n\n*****/***** Your browser name was not valid, \n please re-execute script and provide another valid browser name *****/*****")
    common_ui_actions.maximize_popup(driver)
    print("\n*****/***** Popped up screen was maximized *****/*****")
    return driver


# this method will get the inputted value from CLI
def pytest_addoption(parser):
    parser.addoption("--browser")


# this method will return the inputted browser value to setup method
@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

"""
