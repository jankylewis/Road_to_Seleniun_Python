import logging

from spo.spofrag_common_handler.commonfrag_constant.message_list import LogConstants as log_const
from spo.spofrag_common_handler.commonfrag_constant.constant import Constant as const


class Logging:

    def __init__(self) -> None:
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    @staticmethod
    def log_test_stt(test_name: str,
                     test_stt: str = const.TC_FAILED_STT):
        if test_stt is const.TC_PASSED_STT:

            # log infor
            print(f"\n{test_name} went with {const.TC_PASSED_STT} status\n")
        elif test_stt is const.TC_FAILED_STT:
            print(f"\n{test_name} went with {const.TC_FAILED_STT} status\n")
        else:
            raise SyntaxError

    @staticmethod
    def log_debug(log_msg: str = log_const.get_informative_type()) -> None:
        logging.debug(f"- {log_msg}")

    @staticmethod
    def log_infor(log_msg: str = log_const.get_informative_type()):
        logging.info(f"- {log_msg}")

    @staticmethod
    def log_warning(log_msg: str = log_const.get_warning_type()) -> None:
        logging.info(f"- {log_msg}")

    @staticmethod
    def log_error(log_msg: str = log_const.get_error_type()) -> None:
        logging.info(f"- {log_msg}")

    @staticmethod
    def log_critical(log_msg: str = log_const.get_critical_type()) -> None:
        logging.info(f"- {log_msg}")
