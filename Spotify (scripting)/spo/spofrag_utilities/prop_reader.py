import configparser

# read data from global_var.ini file
config = configparser.RawConfigParser()

config.read("spo/spofrag_env_config/global_var.ini")


class ReadGlobalVar:
    @staticmethod
    def get_app_url() -> str:
        app_url = config.get("common_data", "base_url")
        return app_url

    @staticmethod
    def get_user_email_or_username() -> str:
        usr_email_or_username = config.get("common_data", "user_email_or_username")
        return usr_email_or_username

    @staticmethod
    def get_user_password() -> str:
        usr_pwd = config.get("common_data", "user_password")
        return usr_pwd

    @staticmethod
    def get_browser_type() -> str:
        br = config.get("browser_type", "browser")
        return br
