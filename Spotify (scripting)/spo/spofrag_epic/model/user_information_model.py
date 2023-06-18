from datetime import datetime


class UserInformationModel:
    __user_email_or_username: str
    __user_password: str
    __user_dob: datetime
    __user_nation: str

    def __init__(self, user_email_or_username, user_password, user_dob, user_nation):
        self.__user_email_or_username = user_email_or_username
        self.__user_password = user_password
        self.__user_dob = user_dob
        self.__user_nation = user_nation

    def get_user_email_or_username(self):
        return self.__user_email_or_username

    def set_user_email_or_username(self, user_email_or_username):
        self.__user_email_or_username = user_email_or_username

    def get_user_password(self):
        return self.__user_password

    def set_user_password(self, user_password):
        self.__user_password = user_password

    def get_user_dob(self):
        return self.__user_dob

    def set_user_dob(self, user_dob):
        self.__user_dob = user_dob

    def get_user_nation(self):
        return self.__user_nation

    def set_user_nation(self, user_nation):
        self.__user_nation = user_nation
