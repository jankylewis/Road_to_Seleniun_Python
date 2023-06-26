from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import *
from spo.spofrag_common_handler.assertion_handler import AssertionHandler as asserter
from spo.spofrag_epic.page_object.abstract_pom import Locator_Type as locator_type


class AccountInformationPOM:
    driver_factory = None

    def __init__(self, driver_factory) -> None:
        self.driver_factory = driver_factory

    # there is no other way but getting index
    elements_dict = {
        "LBL_EMAIL_OR_USERNAME": (locator_type.get_xpath_type(), "//tr[2]//td[2]"),
        "LBL_DOB": (locator_type.get_xpath_type(), "//tr[3]//td[2]"),
        "LBL_NATION": (locator_type.get_xpath_type(), "//tr[4]//td[2]"),
    }

    def get_lbl_email_or_username(self) -> WebElement:
        # element_situated: WebElement = AccountInformationPOM.elements_dict.get(
        #     "LBL_EMAIL_OR_USERNAME"
        # )
        if asserter.verify_element_is_visible(
            self.driver_factory,
            exp_element=AccountInformationPOM.elements_dict.get(
                "LBL_EMAIL_OR_USERNAME"
            ),
        ):
            # return element_situated
            return AccountInformationPOM.elements_dict.get("LBL_EMAIL_OR_USERNAME")

    def get_lbl_dob(self) -> WebElement:
        element_situated: WebElement = AccountInformationPOM.elements_dict.get(
            "LBL_DOB"
        )
        if asserter.verify_element_is_visible(
            self.driver_factory, exp_element=element_situated
        ):
            return element_situated

    def get_lbl_nation(self) -> WebElement:
        element_situated: WebElement = AccountInformationPOM.elements_dict.get(
            "LBL_NATION"
        )
        if asserter.verify_element_is_visible(
            self.driver_factory, exp_element=element_situated
        ):
            return element_situated
