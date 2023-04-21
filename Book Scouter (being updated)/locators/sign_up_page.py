class SignUpPage:
    TXT_EMAIL: str = "//input[contains(@name, 'email')]"
    TXT_PASSWORD: str = "//input[contains(@name, 'password')]"
    BTN_SHOW = ""
    CHK_NEWSLETTER: str = \
        "//div[contains(@class, 'SignUpCheckbox')]//span[following-sibling::span[contains(text(), 'Newsletter')]]"
    CHK_BECOME_PRO: str = \
        "//div[contains(@class, 'SignUpCheckbox')]//span[following-sibling::span[contains(text(), 'Become a Pro')]]"
    BTN_SIGN_UP: str = "//button[@type = 'submit' and contains(@name, 'Sign Up')]"
    BTN_CONTINUE_AMAZON = ""
    BTN_CONTINUE_FACEBOOK = ""
    BTN_CONTINUE_TWITTER = ""
    BTN_CONTINUE_GOGGLE = ""
    BTN_CLOSE = ""
    BTN_FORGOT_PASSWORD = ""
    BTN_LOG_IN = ""
