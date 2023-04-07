class HomePage:
    BTN_LOG_IN = "//span[contains(text(), 'Log in')]"
    BTN_SUBSCRIBE_FOR = "//span[contains(text(), 'SUBSCRIBE')][parent::a[@data-testid='subscribe-button']]"
    BTN_MENU = "//button[@data-test-id='search-button']"
    BTN_SEARCH = "//button[@id='desktop-sections-button']"
    BTN_GO = "//button[@data-test-id='search-submit']"
    TXT_SEARCH = "//input[@data-testid='search-input' and @type='text']"
