import pytest

from selenium import webdriver
from spo.spofrag_utilities.prop_reader import ReadGlobalVar as reader
from spo.spofrag_common_handler.commonfrag_constant.constant import Constant as const

from webdriver_manager.opera import OperaDriverManager


@pytest.fixture(autouse=True)
def test_init():
    __br = __retrieve_br()
    if const.CHROME_BR.capitalize() == __br.capitalize():
        driver_factory = webdriver.Chrome()
    elif const.FIREFOX_BR.capitalize() == __br.capitalize():
        driver_factory = webdriver.Firefox()
    elif const.IE_BR.capitalize() == __br.capitalize():
        driver_factory = webdriver.Ie()
    elif const.EDGE_BR.capitalize() == __br.capitalize():
        driver_factory = webdriver.Edge()
    elif const.OPERA_BR.capitalize() == __br.capitalize():
        # driver_factory = OperaDriverManager.install()
        pass
    elif const.SAFARI_BR.capitalize() == __br.capitalize():
        driver_factory = webdriver.Safari()
    elif const.BRAVE_BR.capitalize() == __br.capitalize():
        # driver_factory = webdriver.Brave()
        pass
    else:
        exit()
    driver_factory.maximize_window()
    return driver_factory


def __retrieve_br() -> str:
    # get br from file of global var initialization
    __br_type = reader.get_browser_type()
    if const.CHROME_BR == __br_type:
        return const.CHROME_BR
    elif const.FIREFOX_BR == __br_type:
        return const.FIREFOX_BR
    elif const.IE_BR == __br_type:
        return const.IE_BR
    elif const.EDGE_BR == __br_type:
        return const.EDGE_BR
    elif const.SAFARI_BR == __br_type:
        return const.SAFARI_BR
    elif const.OPERA_BR == __br_type:
        return const.OPERA_BR
    elif const.BRAVE_BR == __br_type:
        return const.BRAVE_BR
