from spo.spofrag_common_handler.ui_action_handler import UIActionHandler as ui_handler
from spo.spofrag_epic.page_object.log_in_pom import LogInPOM as log_in_pom
from spo.spofrag_utilities.data_type_utils import DataTypeHandler as data_type_handler


class LogInPage(log_in_pom):
    check_passed = False
    driver_factory = None

    def __init__(self, driver_factory):
        super().__init__(driver_factory)
        self.driver_factory = driver_factory

    def log_in(self, usr_emai_or_username, pwd, is_remembered: bool = True):
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
