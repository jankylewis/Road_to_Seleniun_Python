from spo.spofrag_epic.model.user_information_model import UserInformationModel as user_model
from spo.spofrag_common_handler.wait_handler import WaitHandler as waiter


class AccountInformationPage:
    driver_factory = None

    def __init__(self, driver_factory):
        self.driver_factory = driver_factory

    def verify_account_page_presented(self, __user_model: user_model):
        waiter.wait_for_page_fully_loaded(self)





    def verify_account_page_presented(self, exp_usr_email_or_username: str) -> bool:
        waiter.wait_for_page_fully_loaded(self)
        act_usr_email_or_username = ui_handler.get_text_from_element(self, account_pom.elements_dict.get(
            "LBL_EMAIL_OR_USERNAME"))
        act_dob = ui_handler.get_text_from_element(self, account_pom.elements_dict.get("LBL_DOB"))
        act_nation = ui_handler.get_text_from_element(self, account_pom.elements_dict.get("LBL_NATION"))
