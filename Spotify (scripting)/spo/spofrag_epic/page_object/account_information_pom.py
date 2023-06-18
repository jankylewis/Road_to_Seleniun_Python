from selenium.webdriver.common.by import By


class AccountInformationPOM:
    # there is no other way but getting index
    elements_dict = {
        "LBL_EMAIL_OR_USERNAME": (By.XPATH, "//tr[2]//td[2]"),
        "LBL_DOB": (By.XPATH, "//tr[3]//td[2]"),
        "LBL_NATION": (By.XPATH, "//tr[4]//td[2]")
    }
