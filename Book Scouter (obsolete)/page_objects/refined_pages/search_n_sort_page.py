# import commands go here
from locators.refined_pages.search_n_sort_page import SearchNSortPage as search_n_sort_page
from common.common_assertions import CommonAssertions as common_assertions
from common.common_ui_actions import CommonUIActions as common_ui_actions
from common.common_operation_helpers import CommonOperatorHelper as common_ope
from common.common_waitings import CommonWaitings as waiters
from selenium.webdriver.common.by import By
from common.constants import Constants as const


class SearchNSortPage:
    """
    search locators go here
    """
    # search key does not satisfy searching standard
    LBL_SEARCH_TITLE: str = search_n_sort_page.LBL_SEARCH_TITLE
    LBL_SEARCH_ERROR_DES: str = search_n_sort_page.LBL_SEARCH_ERROR_DES
    LBL_NO_MATCHES: str = search_n_sort_page.LBL_SEARCH_TITLE
    LBL_NO_MATCHES_DES: str = search_n_sort_page.LBL_SEARCH_NOT_FOUND
    LBL_CHECK_SPELLING: str = search_n_sort_page.LBL_CHECK_SPELLING
    LBL_CHECK_SPELLING_DES: str = search_n_sort_page.LBL_CHECK_SPELLING_DES
    LBL_FEWER_WORDS: str = search_n_sort_page.LBL_FEWER_WORDS
    LBL_FEWER_WORDS_DES: str = search_n_sort_page.LBL_FEWER_WORDS_DES
    LBL_ENTER_ISBN: str = search_n_sort_page.LBL_ENTER_ISBN
    LBL_ENTER_ISBN_DES: str = search_n_sort_page.LBL_ENTER_ISBN_DES

    # search key has matched
    LBL_BOOK_TITLE: str = search_n_sort_page.LBL_BOOK_TITLE
    LBL_BOOK_AUTHOR: str = search_n_sort_page.LBL_BOOK_AUTHOR
    LBL_BOOK_RELEASED: str = search_n_sort_page.LBL_BOOK_RELEASED

    # sort locators go here
    DDL_SORT_BY: str = search_n_sort_page.DDL_SORT_BY
    DDI_RELEVANCE: str = search_n_sort_page.DDI_RELEVANCE
    DDI_TITLE: str = search_n_sort_page.DDI_TITLE
    DDI_AUTHOR: str = search_n_sort_page.DDI_AUTHOR
    DDI_RELEASED: str = search_n_sort_page.DDI_RELEASED

    # vars
    author_index = 0

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
    def verify_search_result_by_author(self, search_key_by_author: str) -> bool:
        check_author: bool = False
        waiters.wait_element_until_visible(self, SearchNSortPage.LBL_BOOK_AUTHOR, const.TIME_OUT_10S)
        list_of_book_author = self.driver.find_elements(By.XPATH, SearchNSortPage.LBL_BOOK_AUTHOR)
        for author in list_of_book_author:
            print("Book author: " + str(author.text))
        for author in list_of_book_author:
            if common_assertions.verify_string_is_contained(str(author.text).casefold(),
                                                            search_key_by_author.casefold()):
                check_author = True
                # author name contains User's search key -> continue to verify the next author name
                continue
            else:
                # author name does not contain User's search key -> break the loop of verifying
                assert False
        if check_author:
            return True
        else:
            return False
        print("\n")

    def __click_on_ddl_sort_by(self):
        common_ui_actions.click_on_element(self, SearchNSortPage.DDL_SORT_BY)

    def __click_on_ddi_released(self):
        common_ui_actions.click_on_element(self, SearchNSortPage.DDI_RELEASED)

    def execute_sort_by_released(self):
        SearchNSortPage.__click_on_ddl_sort_by(self)
        SearchNSortPage.__click_on_ddi_released(self)

    def verify_sort_result_by_released(self) -> bool:
        check_released = False
        waiters.wait_element_until_visible(self, SearchNSortPage.LBL_BOOK_RELEASED, const.TIME_OUT_10S)
        list_of_book_released: list = self.driver.find_elements(By.XPATH, SearchNSortPage.LBL_BOOK_RELEASED)
        list_of_book_released_by_txt: list = []
        for date in list_of_book_released:
            list_of_book_released_by_txt.append(str(date.text))

        print("List of text: " + str(list_of_book_released_by_txt))

        for index in range(0, len(list_of_book_released_by_txt) - 1):
            greater_month: str = list_of_book_released_by_txt[index+1]
            smaller_month: str = list_of_book_released_by_txt[index]
            if common_ope.compare_date_n_time(greater_month, smaller_month):
                check_released = True
                # books' released date are sorted in ascending order -> continue verifying
                continue
            else:
                # books' released date are not sorted following to ascending order -> break the loop
                assert False
        if check_released:
            return True
        else:
            return False
