from spo.spofrag_common_handler.ui_action_handler import UIActionHandler as ui_handler
from spo.spofrag_epic.page_object.log_in_pom import LogInPOM as log_in_pom
from spo.spofrag_common_handler.wait_handler import WaitHandler as waiter
from spo.spofrag_epic.page_object.account_information_pom import AccountInformationPOM as account_pom
from spo.spofrag_common_handler.assertion_handler import AssertionHandler as asserter
from spo.spofrag_epic.model.user_information_model import UserInformationModel as usr_infor_model
from spo.spofrag_utilities.prop_reader_utils import ReadGlobalVar as reader


class LogInPage:
    check_passed = False

    def __init__(self, driver_factory):
        self.driver_factory = driver_factory
        # model initialization
        usr_infor_model.__init__(
            user_email_or_username=reader.get_user_email_or_username(),
            user_password=reader.get_user_password()
        )

    def log_in(self, usr_email_or_username, pwd, is_remembered: bool = True):
        if not is_remembered:
            if ui_handler.get_text_from_element_by_attribute(self, log_in_pom.elements_dict.get("TG_REMEMBER_ME"),
                                                                 "defaultChecked"):
                ui_handler.click_on_element(self, log_in_pom.elements_dict.get("TG_REMEMBER_ME"))

        # ui_handler.send_key_to_element(self, log_in_pom.elements_dict.get("TXT_EMAIL_OR_USERNAME"),
        #                                usr_email_or_username)
        # ui_handler.send_key_to_element(self, log_in_pom.elements_dict.get("TXT_PASSWORD"), pwd)
        # ui_handler.click_on_element(self, log_in_pom.elements_dict.get("BTN_LOG_IN"))

    def verify(self, exp_usr_email_or_username: str) -> bool:
        waiter.wait_for_page_fully_loaded(self)
        act_usr_email_or_username = ui_handler.get_text_from_element(self, account_pom.elements_dict.get(
            "LBL_EMAIL_OR_USERNAME"))
        act_dob = ui_handler.get_text_from_element(self, account_pom.elements_dict.get("LBL_DOB"))
        act_nation = ui_handler.get_text_from_element(self, account_pom.elements_dict.get("LBL_NATION"))
