from selenium import webdriver

from selenium.webdriver import \
    ChromeOptions, \
    FirefoxOptions, \
    WebKitGTKOptions, \
    IeOptions, \
    EdgeOptions

from spo.spofrag_utilities.prop_reader_utils import ReadGlobalVar as reader
from spo.spofrag_common_handler.commonfrag_constant.constant import Constant as const


class DriverManager:
    driver_factory_used: webdriver = None

    @staticmethod
    def produce_driver() -> webdriver:
        __br = DriverManager.__retrieve_br()
        __opts = DriverManager.__retrieve_br_options()
        __driver_factory: webdriver

        if const.CHROME_BR.capitalize() == __br.capitalize():
            __driver_factory = webdriver.Chrome(__opts)
        elif const.FIREFOX_BR.capitalize() == __br.capitalize():
            __driver_factory = webdriver.Firefox(__opts)
        elif const.IE_BR.capitalize() == __br.capitalize():
            __driver_factory = webdriver.Ie(__opts)
        elif const.EDGE_BR.capitalize() == __br.capitalize():
            __driver_factory = webdriver.Edge(__opts)
        elif const.SAFARI_BR.capitalize() == __br.capitalize():
            __driver_factory = webdriver.Safari(__opts)
        else:
            if __driver_factory is not None:
                __driver_factory.quit()

        return __driver_factory

    @staticmethod
    def set_driver_factory(driver_factory: webdriver):
        DriverManager.driver_factory_used = driver_factory

    @staticmethod
    def get_driver_factory() -> webdriver:
        """

        :rtype: object
        """
        return DriverManager.driver_factory_used

    # specially-designed for edge br
    @staticmethod
    def produce_edge_options() -> EdgeOptions:
        opts = webdriver.EdgeOptions
        opts.add_argument('--disable-blink-features=AutomationControlled')
        opts.add_argument("--proxy-server='direct://'")
        opts.add_argument("--proxy-bypass-list=*")
        opts.add_argument('--ignore-certificate-errors')
        opts.add_argument('--proxy-server=IP_ADRESS:PORT')
        # opts.add_argument('headless')

        return opts

    # specially-designed for ie br
    @staticmethod
    def produce_ie_options() -> IeOptions:
        opts = webdriver.IeOptions()
        opts.add_argument('--disable-blink-features=AutomationControlled')
        opts.add_argument("--proxy-server='direct://'")
        opts.add_argument("--proxy-bypass-list=*")
        opts.add_argument('--ignore-certificate-errors')
        opts.add_argument('--proxy-server=IP_ADRESS:PORT')
        # opts.add_argument('headless')

        return opts

    # specially-designed for safari br
    @staticmethod
    def produce_safari_options() -> WebKitGTKOptions:
        opts = webdriver.WebKitGTKOptions()
        opts.add_argument('--disable-blink-features=AutomationControlled')
        opts.add_argument("--proxy-server='direct://'")
        opts.add_argument("--proxy-bypass-list=*")
        opts.add_argument('--ignore-certificate-errors')
        opts.add_argument('--proxy-server=IP_ADRESS:PORT')
        # opts.add_argument('headless')

        return opts

    # specially-designed for firefox br
    @staticmethod
    def produce_firefox_options() -> FirefoxOptions:
        opts = webdriver.FirefoxOptions()
        opts.add_argument('--disable-blink-features=AutomationControlled')
        opts.add_argument("--proxy-server='direct://'")
        opts.add_argument("--proxy-bypass-list=*")
        opts.add_argument('--ignore-certificate-errors')
        opts.add_argument('--proxy-server=IP_ADRESS:PORT')
        # opts.add_argument('headless')

        return opts

    # specially-designed for chrome br due to the prioritized br
    @staticmethod
    def produce_chrome_options() -> ChromeOptions:
        opts = webdriver.ChromeOptions()
        opts.add_argument("--disable-blink-features=AutomationControlled")
        opts.add_argument("--proxy-server='direct://")
        opts.add_argument("--proxy-bypass-list=*")
        opts.add_argument("--ignore-certificate-errors")
        opts.add_argument("--proxy-server=IP_ADRESS:PORT")

        # opts.add_argument('headless')

        # opts.add_argument("--remote-debugging-port=0")
        opts.add_argument("--no-sandbox")
        # opts.add_argument("--disable-dev-shm-usage")

        return opts

    @staticmethod
    def __retrieve_br_options():
        # get br from file of global var initialization
        __br_type = reader.get_browser_type()
        if const.CHROME_BR == __br_type:
            return DriverManager.produce_chrome_options()
        elif const.FIREFOX_BR == __br_type:
            return DriverManager.produce_firefox_options()
        elif const.IE_BR == __br_type:
            return DriverManager.produce_ie_options()
        elif const.SAFARI_BR == __br_type:
            return DriverManager.produce_safari_options()
        elif const.EDGE_BR == __br_type:
            return DriverManager.produce_edge_options()

    @staticmethod
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
