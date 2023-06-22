from enum import Enum
from selenium.webdriver.common.by import By


class Locator_Type(Enum):
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
        return Locator_Type.ID.value

    @staticmethod
    def get_xpath_type():
        return Locator_Type.XPATH.value

    @staticmethod
    def get_css_type():
        return Locator_Type.CSS.value

    @staticmethod
    def get_link_text_type():
        return Locator_Type.LNK_TEXT.value

    @staticmethod
    def get_partial_link_text_type():
        return Locator_Type.PARTIAL_LNK_TEXT.value

    @staticmethod
    def get_name_type():
        return Locator_Type.NAME.value

    @staticmethod
    def get_tag_name_type():
        return Locator_Type.TAG_NAME.value

    @staticmethod
    def get_class_name_type():
        return Locator_Type.CLASS_NAME.value
