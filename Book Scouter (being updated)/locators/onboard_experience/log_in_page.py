class LogInPage:
    TXT_EMAIL: str = "//input[contains(@name, 'email')]"
    TXT_PASSWORD: str = "//input[contains(@name, 'password')]"
    BTN_LOG_IN: str = "//button[@type = 'submit' and contains(text(), 'Login')]"
    ALE_TOAST_BAD_CREDENTIALS = \
        "//div[@role = 'alert']//div[contains(@class, 'toast-icon')]//following-sibling::div"
    ALE_TOAST_INVALID_PASSWORD = ALE_TOAST_BAD_CREDENTIALS
    BTN_CONTINUE_AMAZON = ""
    BTN_CONTINUE_FACEBOOK = ""
    BTN_CONTINUE_TWITTER = ""
    BTN_CONTINUE_GOGGLE = ""
    HPL_FORGOT_PASSWORD = ""
    HPL_SIGN_UP = ""
    BTN_SHOW = ""
    BTN_CLOSE = ""
    LBL_INPUT_EMAIL_ERR_MSG: str = \
        "//span[contains(@class, 'ErrorMsg')][preceding-sibling::label[contains(text(), 'Email')]]"
    LBL_INPUT_PWD_ERR_MSG: str = \
        "//span[contains(@class, 'ErrorMsg')][preceding-sibling::label[contains(text(), 'Password')]]"
    LBL_INVALID_EMAIL_ERR_MSG: str = LBL_INPUT_EMAIL_ERR_MSG
