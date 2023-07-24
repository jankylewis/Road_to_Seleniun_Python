from enum import Enum


class MessageListConstants:
    # log in page
    ERROR_MESSAGE_OF_WRONG_PASSWORD: str = "Incorrect username or password."


class LogConstants(Enum):
    # log messages
    LOG_DEBUG: str = "DEBUG MESSAGE"
    LOG_INFORMATIVE: str = "INFORMATIVE MESSAGE"
    LOG_WARNING: str = "WARNING MESSAGE"
    LOG_ERROR: str = "ERROR MESSAGE"
    LOG_CRITICAL: str = "CRITICAL MESSAGE"

    @staticmethod
    def get_debug_type() -> str:
        return LogConstants.LOG_DEBUG.value

    @staticmethod
    def get_informative_type() -> str:
        return LogConstants.LOG_INFORMATIVE.value

    @staticmethod
    def get_warning_type() -> str:
        return LogConstants.LOG_WARNING.value

    @staticmethod
    def get_error_type() -> str:
        return LogConstants.LOG_ERROR.value

    @staticmethod
    def get_critical_type() -> str:
        return LogConstants.LOG_CRITICAL.value
