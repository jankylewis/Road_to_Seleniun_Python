from spo.spofrag_exe.abstract_test import test_factory
from spo.spofrag_exe.abstract_test import DriverManager as driver_manager
from spo.spofrag_utilities.prop_reader_utils import ReadGlobalVar as reader
from selenium import webdriver
import pytest


class Test_Music_Playing:
    __base_url = reader.get_app_url()
    driver_factory = None

    def test_music_playing_001(self, test_factory, test_flow):
        self.driver_factory.get(self.__base_url)

    @pytest.fixture(autouse=True, scope="")
    def test_flow(self) -> webdriver:
        self.driver_factory = driver_manager.get_driver_factory()
        return self.driver_factory
