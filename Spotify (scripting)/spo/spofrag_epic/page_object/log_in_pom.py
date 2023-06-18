from selenium.webdriver.common.by import By


class LogInPOM:
    elements_dict = {
        "TXT_EMAIL_OR_USERNAME": (By.ID, "login-username"),
        "TXT_PASSWORD": (By.ID, "login-password"),
        "BTN_LOG_IN": (By.ID, "login-button"),
        "TG_REMEMBER_ME": (By.XPATH, "//div[@data-testid = 'login-container']//input[@id = 'login-remember']")
    }
