from spo.spofrag_epic.page_object.abstract_pom import LocatorType as locator_type
from spo.spofrag_common_handler.assertion_handler import AssertionHandler as verifier

from selenium.webdriver.remote.webelement import WebElement


class MusicSearchPOM:
    driver_factory = None

    def __init__(self, driver_factory):
        self.driver_factory = driver_factory

    elements_dict = {
        "TXT_SEARCH": (locator_type.get_xpath_type(), "//input[@data-testid='search-input']")
    }

    def get_txt_search(self) -> WebElement:
        if verifier.verify_element_is_visible(self.driver_factory, MusicSearchPOM.elements_dict.get("TXT_SEARCH")):

            return MusicSearchPOM.elements_dict.get("TXT_SEARCH")
