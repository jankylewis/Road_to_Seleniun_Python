import time

import pytest
from selenium import webdriver
from spo.spofrag_exe.abstract_test import test_factory, driver_manager, AbstractTest
from spo.spofrag_utilities.prop_reader_utils import ReadGlobalVar as reader
from spo.spofrag_common_handler.commonfrag_constant.constant import Constant as const

from spo.spofrag_epic.functionality.music_search_page import MusicSearchPage as music_search_page
from spo.spofrag_epic.functionality.log_in_page import LogInPage as log_in_page


class Test_Music_Playing(AbstractTest):
    driver_factory = None

    __base_url = reader.get_app_url()
    __log_in_url = __base_url + const.LOG_IN_PATH
    __search_url = reader.get_public_url() + const.SEARCH_PATH

    __test_name: str

    @pytest.mark.order(1)
    def test_music_playing_001(self, test_factory: None):
        # search music
        # music_search_page.search_by_term(self, "See You Again")

        time.sleep(100000)

    @classmethod
    @pytest.mark.usefixtures("test_factory")
    def setup_method(cls, method) -> webdriver:
        test_address: str = f"{type(cls).__name__} -> {method.__name__}"
        cls.__test_name = test_address

        cls.driver_factory = driver_manager.get_driver_factory()

        # log in
        cls.driver_factory.get(cls.__log_in_url)
        cls.log_in(cls)

        # cls.driver_factory.get(cls.__search_url)

        return cls.driver_factory

    def log_in(self):
        """

        :rtype: object
        """
        log_in_page.log_in(self,
                           reader.get_user_email_or_username(),
                           reader.get_user_password(),
                           False)
