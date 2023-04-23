class Constants:
    # Timeout variables for waiting methods by second
    TIME_OUT_1S: int = 1
    TIME_OUT_2S: int = 2
    TIME_OUT_3S: int = 3
    TIME_OUT_5S: int = 5
    TIME_OUT_10S: int = 10
    TIME_OUT_15S: int = 15
    MIN_TIME_OUT: float = 0.5
    MAX_TIME_OUT: int = 30

    # test case classifications
    TC_PASS_STATUS: str = "p"
    TC_FAILED_STATUS: str = "f"
    TC_LOG_IN_FUNCTION: str = "Log in"
    TC_SIGN_UP_FUNCTION: str = "Sign up"

    # browser types
    CHROME_BR: str = "chrome"
    FIREFOX_BR: str = "firefox"
    IE_BR: str = "ie"
    EDGE_BR: str = "edge"
    SAFARI_BR: str = "safari"
    OPERA_BR: str = "opera"
    BRAVE_BR: str = "brave"

    # Attribute value facilitating getting content from UI
    ATTRIBUTE_VALUE: str = "value"

    """
    Text messages locate here
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
