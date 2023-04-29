class SearchNSortPage:
    """
    those below captured for flow: search key causes errors
    """
    LBL_SEARCH_TITLE: str = "//h2[not(contains(@class, 'SearchTips'))]"
    LBL_SEARCH_ERROR_DES: str = "//p[contains(@class, 'ErrorText')]"
    # happen when User's search key did not match any result
    LBL_SEARCH_TIPS: str = "//h2[contains(@class, 'SearchTips')]"
    LBL_SEARCH_NOT_FOUND: str = "//p[contains(@class, 'SearchText')]"
    IMG_CHECK_SPELLING: str
    LBL_CHECK_SPELLING: str = \
        "//div[contains(@data-test-id, 'SearchPage')]//p[contains(text(), 'Check the spelling')]"
    LBL_CHECK_SPELLING_DES: str = \
        "//div[contains(@data-test-id, 'SearchPage')]//p[contains(text(), 'Check the spelling')]//following-sibling::p[contains(@class, 'Content')]"
    # LBL_CHECK_SPELLING_DES: str = "//div[contains(@data-test-id, 'SearchPage')]//p[contains(text(), 'Check the spelling')]//following-sibling::p[contains(@class, 'Content') or not(contains(@class, 'Content'))]"
    LBL_FEWER_WORDS: str = \
        "//div[contains(@data-test-id, 'SearchPage')]//p[contains(text(), 'Use fewer words')]"
    LBL_FEWER_WORDS_DES: str = \
        "//div[contains(@data-test-id, 'SearchPage')]//p[contains(text(), 'Use fewer words')]//following-sibling::p[contains(@class, 'Content')]"
    IMG_FEWER_WORDS: str
    LBL_ENTER_ISBN: str = \
        "//div[contains(@data-test-id, 'SearchPage')]//p[contains(text(), 'Enter an ISBN')]"
    LBL_ENTER_ISBN_DES: str = \
        "//div[contains(@data-test-id, 'SearchPage')]//p[contains(text(), 'Enter an ISBN')]//following-sibling::p[contains(@class, 'Content')]"
    IMG_ENTER_ISBN: str
    """
    those below captured for flow: search key found and returned list of results if any of search key matched (may satisfy several criteria)
    """
    LBL_SEARCH_KEY_HIGHLIGHT: str = "//p[contains(@class, 'SearchTitleHighlight')]"
    LBL_BOOK_TITLE: str = "//h2[contains(@class, 'BookTitle')]"
    LBL_BOOK_AUTHOR: str = "//span[contains(@class, 'BookText')][preceding-sibling::strong[contains(text(), 'Author')]]"
    LBL_BOOK_RELEASED: str = "//span[contains(@class, 'BookText')][preceding-sibling::strong[contains(text(), 'Released')]]"
    LBL_BOOK_ISBN: str = ""
    """
    those below for sort case
    """
    DDL_SORT_BY: str = "//div[contains(@aria-label, 'Select sort by')]"
    DDI_RELEVANCE: str = "//ul[contains(@class, 'options')]//li[contains(text(), 'Relevance')]"
    DDI_TITLE: str = "//ul[contains(@class, 'options')]//li[contains(text(), 'Title')]"
    DDI_AUTHOR: str = "//ul[contains(@class, 'options')]//li[contains(text(), 'Author')]"
    DDI_RELEASED: str = "//ul[contains(@class, 'options')]//li[contains(text(), 'Released')]"




