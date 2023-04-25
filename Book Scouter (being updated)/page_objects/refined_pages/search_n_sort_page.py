# import commands go here
from locators.refined_pages.search_n_sort_page import SearchNSortPage as search_page
from common.common_assertions import CommonAssertions as common_assertions
from common.common_ui_actions import CommonUIActions as common_ui_actions
from common.constants import Constants as const


class SearchNSortPage:
    """
    locators go here
    """
    # search key does not satisfy searching standard
    LBL_SEARCH_TITLE: str = search_page.LBL_SEARCH_TITLE
    LBL_SEARCH_ERROR_DES: str = search_page.LBL_SEARCH_ERROR_DES
    LBL_NO_MATCHES: str = search_page.LBL_SEARCH_TITLE
    LBL_NO_MATCHES_DES: str = search_page.LBL_SEARCH_NOT_FOUND
    LBL_CHECK_SPELLING: str = search_page.LBL_CHECK_SPELLING
    LBL_CHECK_SPELLING_DES: str = search_page.LBL_CHECK_SPELLING_DES
    LBL_FEWER_WORDS: str = search_page.LBL_FEWER_WORDS
    LBL_FEWER_WORDS_DES: str = search_page.LBL_FEWER_WORDS_DES
    LBL_ENTER_ISBN: str = search_page.LBL_ENTER_ISBN
    LBL_ENTER_ISBN_DES: str = search_page.LBL_ENTER_ISBN_DES

    def __init__(self, driver):
        self.driver = driver

    # search key does not satisfy searching standard
    # verification methods go here
    def __verify_err_title(self) -> bool:
        exp_err_title = const.LBL_ERR_SEARCH_TITLE
        act_err_title = common_ui_actions.get_text_from_element(self, SearchNSortPage.LBL_SEARCH_TITLE)
        if common_assertions.verify_string_is_equal(exp_err_title, act_err_title):
            print(f"The expected error title <{exp_err_title}> matched the actual <{act_err_title}>.")
            return True
        else:
            print(f"The expected error title <{exp_err_title}> did not match the actual <{act_err_title}>.")
            return False

    def __verify_err_des(self) -> bool:
        exp_err_title = const.LBL_ERR_SEARCH_DES
        act_err_title = common_ui_actions.get_text_from_element(self, SearchNSortPage.LBL_SEARCH_ERROR_DES)
        if common_assertions.verify_string_is_equal(exp_err_title, act_err_title):
            print(f"The expected error description <{exp_err_title}> matched the actual <{act_err_title}>.")
            return True
        else:
            print(f"The expected error description <{exp_err_title}> did not match the actual <{act_err_title}>.")
            return False

    def verify_err(self) -> bool:
        if SearchNSortPage.__verify_err_title(self) and SearchNSortPage.__verify_err_des(self):
            print("Search page SUCCESSFULLY verified.")
            return True
        else:
            print("Search page verified FAILED.")
            return False

    # search key does not match any returned result from website
    # verification methods go here
    def __verify_err_no_matches_title(self) -> bool:
        exp_no_matches_title = const.LBL_ERR_NO_MATCHES
        act_no_matches_title = common_ui_actions.get_text_from_element(self, SearchNSortPage.LBL_NO_MATCHES)
        if common_assertions.verify_string_is_equal(exp_no_matches_title, act_no_matches_title):
            print(
                f"The non-result expected error <{exp_no_matches_title}> matched the actual <{act_no_matches_title}>.")
            return True
        else:
            print(
                f"The non-result expected error <{exp_no_matches_title}> did not match the actual <{act_no_matches_title}>.")
            return False

    def __verify_err_no_matches_des(self) -> bool:
        exp_no_matches_des = const.LBL_ERR_NO_MATCHES_DES
        act_no_matches_des = common_ui_actions.get_text_from_element(self, SearchNSortPage.LBL_NO_MATCHES_DES)
        if common_assertions.verify_string_is_equal(exp_no_matches_des, act_no_matches_des):
            print(
                f"The non-result expected error description <{exp_no_matches_des}> matched the actual <{act_no_matches_des}>.")
            return True
        else:
            print(
                f"The non-result expected error description <{exp_no_matches_des}> did not match the actual <{act_no_matches_des}>.")
            return False

    def verify_err_no_matches(self) -> bool:
        if SearchNSortPage.__verify_err_no_matches_title(self) and SearchNSortPage.__verify_err_no_matches_des(self):
            print("Search page SUCCESSFULLY verified.")
            return True
        else:
            print("Search page verified FAILED.")
            return False

    # returned result of search page contains search key
    # verification for successful cases go here
