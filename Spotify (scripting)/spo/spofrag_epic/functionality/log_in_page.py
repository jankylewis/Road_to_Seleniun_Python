import time

from spo.spofrag_common_handler.ui_action_handler import UIActionHandler as ui_handler
from spo.spofrag_epic.page_object.log_in_pom import LogInPOM as log_in_pom
from spo.spofrag_utilities.data_type_utils import DataTypeHandler as data_type_handler
from spo.spofrag_common_handler.assertion_handler import AssertionHandler as verifier
from spo.spofrag_common_handler.commonfrag_constant.message_list import MessageListConstants as msg_const


class LogInPage(log_in_pom):
    check_passed = False
    driver_factory = None

    def __init__(self, driver_factory):
        super().__init__(driver_factory)
        self.driver_factory = driver_factory

    def log_in(self, usr_emai_or_username, pwd, is_remembered: bool = True):
        """

        :rtype: object
        """
        LogInPage.__set_remember_me_toggle(self, is_remembered)
        ui_handler.send_key_to_element(self, log_in_pom.get_txt_email_or_username(self),
                                       usr_emai_or_username)
        ui_handler.send_key_to_element(self, log_in_pom.get_txt_password(self), pwd)
        ui_handler.click_on_element(self, log_in_pom.get_btn_login(self))

    def __set_remember_me_toggle(self, is_remembered: bool):
        df_checking: bool = data_type_handler.cast_to_bool(
            ui_handler.get_value_from_element_by_attribute(self, log_in_pom.get_tg_remember_me_df_checked(self),
                                                           "defaultChecked"))

        if df_checking is not is_remembered:
            ui_handler.scroll_into_element_by_js(self, log_in_pom.get_tg_remember_me(self))
            ui_handler.click_on_element(self, log_in_pom.get_tg_remember_me(self))

    def verify_log_in_unsuccessfully(self) -> bool:
        __is_checked: bool = False

        act_txt_of_err_msg: str = ui_handler.get_text_from_element(self, log_in_pom.get_txt_err_msg_of_wrong_pwd(self))
        if verifier.verify_string_is_equal(exp_str=msg_const.ERROR_MESSAGE_OF_WRONG_PASSWORD,
                                           act_str=act_txt_of_err_msg):
            return not __is_checked
        else:
            return __is_checked
