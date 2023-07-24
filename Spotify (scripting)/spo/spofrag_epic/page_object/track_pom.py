from selenium.webdriver.remote.webelement import WebElement

from spo.spofrag_epic.page_object.abstract_pom import LocatorType as locator_type
from spo.spofrag_common_handler.wait_handler import WaitHandler as waiter


class TrackPOM:
    driver_factory = None

    def __init__(self, driver_factory):
        self.driver_factory = driver_factory

    elements_dict = {
        "BTN_PLAY_TRACK": (locator_type.get_xpath_type(),
                           "//button[@data-encore-id = 'buttonTertiary'][span]//preceding-sibling::div//button[@data-testid = 'play-button']")
    }

    def get_btn_play_track(self) -> WebElement:
        return waiter.wait_element_until_visible(self.driver_factory,
                                                 TrackPOM.elements_dict.get("BTN_PLAY_TRACK"))
