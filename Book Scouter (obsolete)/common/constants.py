class Constants:
    # timeout variables for waiting methods by second
    TIME_OUT_1S: int = 1
    TIME_OUT_2S: int = 2
    TIME_OUT_3S: int = 3
    TIME_OUT_5S: int = 5
    TIME_OUT_10S: int = 10
    TIME_OUT_15S: int = 15
    MIN_TIME_OUT: float = 0.5
    MAX_TIME_OUT: int = 30

    # test case classifications
    TC_PASSED_STATUS: str = "p"
    TC_FAILED_STATUS: str = "f"
    TC_LOG_IN_FUNCTION: str = "Log in"
    TC_SIGN_UP_FUNCTION: str = "Sign up"
    TC_SEARCH_FUNCTION: str = "Search"
    TC_SORT_FUNCTION: str = "Sort"

    # browser types
    CHROME_BR: str = "chrome"
    FIREFOX_BR: str = "firefox"
    IE_BR: str = "ie"
    EDGE_BR: str = "edge"
    SAFARI_BR: str = "safari"
    OPERA_BR: str = "opera"
    BRAVE_BR: str = "brave"

    # attribute value facilitating getting content from UI
    ATTRIBUTE_VALUE: str = "value"

    # keys to press
    KEY_ENTER = "enter"
    KEY_BACKSPACE = "backspace"
    KEY_TAB = "tab"
    KEY_SHIFT = "shift"
    KEY_RETURN = "return"
    KEY_CONTROL = "control"
    KEY_LEFT_CONTROL = "left control"
    KEY_LEFT_SHIFT = "left shift"
    KEY_ALT = "alt"
    KEY_LEFT_ALT = "left alt"
    KEY_PAUSE = "pause"
    KEY_ESCAPE = "escape"
    KEY_SPACE = "space"
    KEY_PAGE_UP = "page up"
    KEY_PAGE_DOWN = "page down"
    KEY_END = "end"
    KEY_HOME = "home"
    KEY_LEFT = "left"
    KEY_UP = "up"
    KEY_RIGHT = "right"
    KEY_DOWN = "down"
    KEY_ARROW_LEFT = "arrow left"
    KEY_ARROW_UP = "arrow up"
    KEY_ARROW_RIGHT = "arrow right"
    KEY_ARROW_DOWN = "arrow down"
    KEY_INSERT = "insert"
    KEY_DELETE = "delete"
    KEY_SEMICOLON = "semicolon"
    KEY_EQUALS = "equals"
    KEY_NUMPAD_0 = "0"
    KEY_NUMPAD_1 = "1"
    KEY_NUMPAD_2 = "2"
    KEY_NUMPAD_3 = "3"
    KEY_NUMPAD_4 = "4"
    KEY_NUMPAD_5 = "5"
    KEY_NUMPAD_6 = "6"
    KEY_NUMPAD_7 = "7"
    KEY_NUMPAD_8 = "8"
    KEY_NUMPAD_9 = "9"
    KEY_MULTIPLY = "multiply"
    KEY_ADD = "add"
    KEY_SEPARATOR = "separator"
    KEY_SUBTRACT = "subtract"
    KEY_DECIMAL = "decimal"
    KEY_DIVIDE = "divide"
    KEY_F1 = "f1"
    KEY_F2 = "f2"
    KEY_F3 = "f3"
    KEY_F4 = "f4"
    KEY_F5 = "f5"
    KEY_F6 = "f6"
    KEY_F7 = "f7"
    KEY_F8 = "f8"
    KEY_F9 = "f9"
    KEY_F10 = "f10"
    KEY_F11 = "f11"
    KEY_F12 = "f12"
    # META = "meta"
    # COMMAND = "command"
    # ZENKAKU_HANKAKU = "zenkaku_hankaku"


    """
    Text messages go here
    """
    # log-in page
    INVALID_PASSWORD: str = "The presented password is invalid."
    BAD_CREDENTIALS: str = "Bad credentials."
    EXISTED_EMAIL: str = "Email: user already signed up."
    # toast notification
    SUCCESSFULLY_LOG_IN: str = "You've successfully logged in."
    INPUT_EMAIL_ERR_MSG: str = "Please enter your email address"
    INPUT_PWD_ERR_MSG: str = "Please enter your password"
    INVALID_EMAIL_ERR_MSG: str = "Please enter a valid email address"
    INVALID_PWD_ERR_MSG: str = "Password must be at least 6 characters long"
    INVALID_CC_NUMBER: str = "Invalid card number"
    INVALID_EXPIRED_DATE: str = "Invalid expiration date"
    INVALID_CVC: str = "Invalid security code"
    INVALID_DECLINED_CARD = "Your card was declined. Your request was in live mode, but used a known test card."

    """
    search page
    """
    # search key not gratify website's searching standard
    LBL_ERR_SEARCH_TITLE = "Invalid search key"  # just an assumption
    LBL_ERR_SEARCH_DES = "The length of search key must be greater than or equal to 3"
    # search key not found even User gratified website's searching standard
    LBL_ERR_NO_MATCHES = "No Matches..."
    LBL_ERR_NO_MATCHES_DES = \
        "Unfortunately, there weren't any matches for your search. Please check your title or use the ISBN for the book."
    LBL_TIPS = "Tips to help you find the book on BookScouter"
    LBL_CHECK_SPELLING = "Check the spelling"
    LBL_CHECK_SPELLING_DES = \
        "Please check the search form up above for squiggly red lines that indicate a misspelling. " \
        "Sometimes you can right mouse click or tap the misspelled word for suggestions."
    LBL_FEWER_WORDS = "Use fewer words"
    LBL_FEWER_WORDS_DES = "Sometimes it helps to try fewer words in your search. Just the title often works best"
    LBL_ENTER_ISBN = "Enter an ISBN"
    LBL_ENTER_ISBN_DES = "Most books published after 1975 have a 10 or 13 digit number assigned to them. " \
                         "Maybe you can gain access to a copy of the book you are looking for. " \
                         "If so, use the ISBN to find the exact same edition."
