from datetime import datetime
from spo.spofrag_utilities.data_faker import FakeDataGenerator as faker


class UserInformationModel:
    __user_email_or_username: str = faker.produce_fake_name()
    __user_dob: str or datetime = faker.produce_fake_date()
    __user_nation: str = faker.produce_fake_nation()

    def __init__(self, user_email_or_username, user_dob, user_nation):
        self.__user_email_or_username = user_email_or_username
        self.__user_dob = user_dob
        self.__user_nation = user_nation

    def get_user_email_or_username(self) -> type(__user_email_or_username):
        return self.__user_email_or_username

    def set_user_email_or_username(self, user_email_or_username):
        self.__user_email_or_username = user_email_or_username

    def get_user_dob(self) -> type(__user_dob):
        return self.__user_dob

    def set_user_dob(self, user_dob):
        self.__user_dob = user_dob

    def get_user_nation(self) -> type(__user_nation):
        return self.__user_nation

    def set_user_nation(self, user_nation):
        self.__user_nation = user_nation
