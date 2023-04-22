import configparser

# read data from global_variables.ini file
config = configparser.RawConfigParser()

# global_variables.ini path
# config.read("/Users/vinhtran02092k/Desktop/practice_projects/Selenium_Python/Book Scouter/env_configurations/global_variables.ini")
config.read("env_configurations/global_variables.ini")


class ReadGlobalVariables:
    @staticmethod
    def get_application_url() -> str:
        url = config.get('common data', 'base_url')
        return url

    @staticmethod
    def get_user_email() -> str:
        user_email = config.get("common data", "user_email")
        return user_email

    @staticmethod
    def get_user_password() -> str:
        user_password = config.get("common data", "user_password")
        return user_password

    @staticmethod
    def get_cc_number() -> str:
        cc_number = config.get("credit card data", "cc_number")
        return cc_number

    @staticmethod
    def get_expired_date() -> str:
        expired_date = config.get("credit card data", "expired date")
        return expired_date

    @staticmethod
    def get_cvc() -> str:
        cvc = config.get("credit card data", "expired date")
        return cvc
