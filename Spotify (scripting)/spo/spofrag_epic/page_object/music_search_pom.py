from spo.spofrag_epic.page_object.abstract_pom import LocatorType as locator_type
from spo.spofrag_common_handler.assertion_handler import AssertionHandler as verifier

from spo.spofrag_common_handler.commonfrag_constant.constant import Constant as const

from selenium.webdriver.remote.webelement import WebElement


class MusicSearchPOM:
    driver_factory = None

    def __init__(self, driver_factory):
        self.driver_factory = driver_factory

    elements_dict = {
        "TXT_SEARCH": (locator_type.get_xpath_type(), "//input[@data-testid='search-input']"),
        "BTN_PLAY_AT_TOP_RESULT": (locator_type.get_xpath_type(),
                                   "//div[@data-testid = 'top-result-card']//button[@data-testid= 'play-button'][span[contains(@class, 'Button')]]")
    }

    def get_txt_search(self) -> WebElement:
        if verifier.verify_element_is_visible(self.driver_factory, MusicSearchPOM.elements_dict.get("TXT_SEARCH")):
            return MusicSearchPOM.elements_dict.get("TXT_SEARCH")

    def get_btn_play_at_top_result(self) -> WebElement:
        if verifier.verify_element_is_visible(self.driver_factory,
                                              (locator_type.get_xpath_type(),
                                               "//div[@data-testid = 'top-result-card']//button[@data-testid= 'play-button'][span[contains(@class, 'Button')]]"),
                                              time_out=const.TIME_OUT_15S,
                                              is_long_wait=True):
            return MusicSearchPOM.elements_dict.get("BTN_PLAY_AT_TOP_RESULT")
