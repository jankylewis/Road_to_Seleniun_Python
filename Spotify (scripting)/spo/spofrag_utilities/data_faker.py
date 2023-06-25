from faker import Faker
import datetime


class FakeDateGenerator:
    data_producer = Faker()

    @staticmethod
    def produce_fake_nation() -> str:
        return FakeDateGenerator.data_producer.country()

    @staticmethod
    def produce_fake_date(start_date: str = "today", end_date: str = "+5y") -> datetime:
        return FakeDateGenerator.data_producer.date_between(start_date=start_date, end_date=end_date)

    @staticmethod
    def produce_fake_name() -> str:
        return FakeDateGenerator.data_producer.name()

    @staticmethod
    def produce_fake_text(number_of_chars: int = 10) -> str:
        if number_of_chars < 5:
            number_of_chars = 5
            return FakeDateGenerator.data_producer.text(number_of_chars)
        else:
            return FakeDateGenerator.data_producer.text(number_of_chars)
