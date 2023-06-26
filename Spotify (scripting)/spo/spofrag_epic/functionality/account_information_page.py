from spo.spofrag_epic.model.user_information_model import (
    UserInformationModel as user_model,
)
from spo.spofrag_common_handler.wait_handler import WaitHandler as waiter
from spo.spofrag_common_handler.ui_action_handler import UIActionHandler as ui_handler
from spo.spofrag_epic.page_object.account_information_pom import (
    AccountInformationPOM as account_pom,
)
from spo.spofrag_common_handler.assertion_handler import AssertionHandler as asserter
from spo.spofrag_common_handler.commonfrag_constant.constant import Constant as const


class AccountInformationPage:
    driver_factory = None

    def __init__(self, driver_factory):
        self.driver_factory = driver_factory

    def verify_account_page_presented(self, __user_model: user_model) -> bool:
        __is_check: bool = False

        waiter.wait_for_page_fully_loaded(AccountInformationPage.driver_factory)
        # waiter.wait_element_until_visible(
        #     AccountInformationPage.driver_factory,
        #     AccountInformationPOM.elements_dict.get("LBL_EMAIL_OR_USERNAME"),
        #     const.TIME_OUT_10S,
        # )
        waiter.force_wait(self, 10.5)

        act_usr_email_or_username: str = ui_handler.get_text_from_element(
            self, account_pom.get_lbl_email_or_username(self)
        )
        act_dob: str = ui_handler.get_text_from_element(
            self, account_pom.get_lbl_dob(self)
        )
        act_nation: str = ui_handler.get_text_from_element(
            self, account_pom.get_lbl_nation(self)
        )

        # verifying
        if (
            asserter.verify_string_is_equal(
                user_model.get_user_email_or_username(self), act_usr_email_or_username
            )
            and asserter.verify_datetime(user_model.get_user_dob(self), act_dob)
            and asserter.verify_string_is_equal(
                user_model.get_user_nation(self), act_nation
            )
        ):
            return not __is_check
        else:
            return __is_check
