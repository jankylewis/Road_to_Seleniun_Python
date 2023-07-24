from selenium.webdriver.remote.webelement import *
from spo.spofrag_common_handler.assertion_handler import AssertionHandler as asserter
from spo.spofrag_epic.page_object.abstract_pom import LocatorType as locator_type


class AccountInformationPOM:
    driver_factory = None

    def __init__(self, driver_factory) -> None:
        self.driver_factory = driver_factory

    # there is no other way but getting index
    elements_dict = {
        "LBL_EMAIL_OR_USERNAME": (locator_type.get_xpath_type(), "//tr[2]//td[2]"),
        "LBL_DOB": (locator_type.get_xpath_type(), "//tr[3]//td[2]"),
        "LBL_NATION": (locator_type.get_xpath_type(), "//tr[4]//td[2]"),
        "BTN_SPOTIFY_LOGO": (locator_type.get_xpath_type(), "//a[contains(@data-tracking, 'spotify-logo')]")
    }

    def get_btn_spotify_logo(self) -> WebElement:
        if asserter.verify_element_is_visible(self.driver_factory, exp_element=AccountInformationPOM.elements_dict.get(
                "BTN_SPOTIFY_LOGO")):
            return AccountInformationPOM.elements_dict.get("BTN_SPOTIFY_LOGO")

    def get_lbl_email_or_username(self) -> object:
        if asserter.verify_element_is_visible(self.driver_factory, exp_element=AccountInformationPOM.elements_dict.get(
                "LBL_EMAIL_OR_USERNAME")):
            return AccountInformationPOM.elements_dict.get("LBL_EMAIL_OR_USERNAME")

    def get_lbl_dob(self) -> WebElement:
        AccountInformationPOM.elements_dict.get("LBL_DOB")
        if asserter.verify_element_is_visible(self.driver_factory,
                                              exp_element=AccountInformationPOM.elements_dict.get("LBL_DOB")):
            return AccountInformationPOM.elements_dict.get("LBL_DOB")

    def get_lbl_nation(self) -> WebElement:

        if asserter.verify_element_is_visible(self.driver_factory,
                                              exp_element=AccountInformationPOM.elements_dict.get("LBL_NATION")):
            return AccountInformationPOM.elements_dict.get("LBL_NATION")
