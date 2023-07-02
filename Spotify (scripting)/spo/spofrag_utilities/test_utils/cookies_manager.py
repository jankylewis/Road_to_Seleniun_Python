from selenium import webdriver


class CookiesManager:
    __cookies_list: list = None

    @staticmethod
    def get_all_cookies(driver_factory: webdriver) -> list:
        CookiesManager.cookies_list = driver_factory.get_cookies()
        return CookiesManager.cookies_list

    @staticmethod
    def delete_all_cookies(driver_factory: webdriver):
        cookies_used: list = CookiesManager.__cookies_list if CookiesManager.__cookies_list is not None else CookiesManager.get_all_cookies(
            driver_factory)

        if cookies_used is not None:
            driver_factory.execute_cdp_cmd('Storage.clearDataForOrigin', {"origin": '*', "storageTypes": 'all', })
