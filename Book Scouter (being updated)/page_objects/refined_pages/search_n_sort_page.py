# import commands go here
from locators.refined_pages.search_n_sort_page import SearchNSortPage as search_page


class SearchNSortPage:
    """
    locators go here
    """
    # search key does not satisfy searching standard
    LBL_SEARCH_TITLE: str = search_page.LBL_SEARCH_TITLE
    LBL_SEARCH_ERROR: str = search_page.LBL_SEARCH_ERROR

    def __init__(self, driver):
        self.driver = driver


