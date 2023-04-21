import configparser

# read data from global_variables.ini file
config = configparser.RawConfigParser()
# global_variables.ini path
# config.read("/Users/vinhtran02092k/Desktop/practice_projects/Selenium_Python/Book Scouter/env_configurations/global_variables.ini")
config.read("env_configurations/global_variables.ini")


class ReadGlobalVariables:
    @staticmethod
    def get_application_url():
        url = config.get('common data', 'base_url')
        return url

    @staticmethod
    def get_user_email():
        user_email = config.get("common data", "user_email")
        return user_email

    @staticmethod
    def get_user_password():
        user_password = config.get("common data", "user_password")
        return user_password
