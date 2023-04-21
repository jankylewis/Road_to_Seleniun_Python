class LogInPage:
    TXT_EMAIL: str = "//input[contains(@name, 'email')]"
    TXT_PASSWORD: str = "//input[contains(@name, 'password')]"
    BTN_LOG_IN: str = "//button[@type = 'submit' and contains(text(), 'Login')]"
    ALE_TOAST_BAD_CREDENTIALS = "//div[@role = 'alert']//div[contains(@class, 'toast-icon')]//following-sibling::div"
    ALE_TOAST_INVALID_PASSWORD = ALE_TOAST_BAD_CREDENTIALS
    BTN_CONTINUE_AMAZON = ""
    BTN_CONTINUE_FACEBOOK = ""
    BTN_CONTINUE_TWITTER = ""
    BTN_CONTINUE_GOGGLE = ""
    HPL_FORGOT_PASSWORD = ""
    HPL_SIGN_UP = ""
    BTN_SHOW = ""
