import logging
from spo.spofrag_common_handler.commonfrag_constant.message_list import MessageListConstants as msg_const


class Logging:

    def __init__(self) -> None:
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    @staticmethod
    def log_debug(log_msg: str = msg_const.LOG_DEBUG) -> None:
        logging.debug(f"- {log_msg}")

    @staticmethod
    def log_infor(log_msg: str = msg_const.LOG_INFOR) -> None:
        logging.info(f"- {log_msg}")

    @staticmethod
    def log_warning(log_msg: str = msg_const.LOG_WARNING) -> None:
        logging.info(f"- {log_msg}")

    @staticmethod
    def log_error(log_msg: str = msg_const.LOG_ERROR) -> None:
        logging.info(f"- {log_msg}")

    @staticmethod
    def log_critical(log_msg: str = msg_const.LOG_CRITICAL) -> None:
        logging.info(f"- {log_msg}")
