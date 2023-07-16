from enum import Enum
from selenium.webdriver.common.by import By


class LocatorType(Enum):
    ID = By.ID
    XPATH = By.XPATH
    CSS = By.CSS_SELECTOR
    LNK_TEXT = By.LINK_TEXT
    PARTIAL_LNK_TEXT = By.PARTIAL_LINK_TEXT
    NAME = By.NAME
    TAG_NAME = By.TAG_NAME
    CLASS_NAME = By.CLASS_NAME

    @staticmethod
    def get_id_type():
        return LocatorType.ID.value

    @staticmethod
    def get_xpath_type():
        return LocatorType.XPATH.value

    @staticmethod
    def get_css_type():
        return LocatorType.CSS.value

    @staticmethod
    def get_link_text_type():
        return LocatorType.LNK_TEXT.value

    @staticmethod
    def get_partial_link_text_type():
        return LocatorType.PARTIAL_LNK_TEXT.value

    @staticmethod
    def get_name_type():
        return LocatorType.NAME.value

    @staticmethod
    def get_tag_name_type():
        return LocatorType.TAG_NAME.value

    @staticmethod
    def get_class_name_type():
        return LocatorType.CLASS_NAME.value
