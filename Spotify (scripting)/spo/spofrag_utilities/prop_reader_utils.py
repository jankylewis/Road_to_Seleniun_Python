import configparser

# read data from global_var.ini file
config = configparser.RawConfigParser()

config.read("spo/spofrag_env_config/global_var.ini")


class ReadGlobalVar:

    @staticmethod
    def get_public_url() -> str:
        public_url = config.get("common_data", "public_url")
        return public_url

    @staticmethod
    def get_app_url() -> str:
        app_url = (
                config.get("common_data", "base_url") + ReadGlobalVar.get_localization()
        )
        return app_url

    @staticmethod
    def get_localization() -> str:
        usr_localized = config.get("common_data", "end_point_localization")
        return usr_localized

    @staticmethod
    def get_user_dob() -> str:
        user_dob = config.get("user_information", "user_dob")
        return user_dob

    @staticmethod
    def get_user_nation() -> str:
        user_nation = config.get("user_information", "user_nation")
        return user_nation

    @staticmethod
    def get_user_email_or_username() -> str:
        usr_email_or_username = config.get("user_information", "user_email_or_username")
        return usr_email_or_username

    @staticmethod
    def get_user_password() -> str:
        usr_pwd = config.get("user_information", "user_password")
        return usr_pwd

    @staticmethod
    def get_browser_type() -> str:
        br = config.get("browser_type", "browser")
        return br
