from datetime import datetime
from enum import Enum


class DateTimeHandler:
    @staticmethod
    def is_time_out(start_time: datetime, time_out: int) -> bool:
        stop: int = int(DateTimeHandler.get_minute(start_time)) + time_out
        if datetime.utcnow().minute < stop:
            return False
        else:
            return True

    @staticmethod
    def get_minute(date_time: datetime):
        return date_time.minute

    @staticmethod
    def get_hour(date_time: datetime):
        return date_time.hour

    @staticmethod
    def get_second(date_time: datetime):
        return date_time.second

    @staticmethod
    def get_minute_now() -> int:
        return datetime.utcnow().minute

    @staticmethod
    def get_second_now() -> int:
        return datetime.utcnow().second

    @staticmethod
    def get_hour_now() -> int:
        return datetime.utcnow().hour

    @staticmethod
    def get_date_time_now() -> datetime:
        return datetime.utcnow()


class DateTimeTransformation(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12

    def get_month_from_str(date_str: str) -> str:
        match int(date_str):
            case int(DateTimeTransformation.January.value):
                return DateTimeTransformation.January.name
            case int(DateTimeTransformation.February.value):
                return DateTimeTransformation.February.name
            case int(DateTimeTransformation.March.value):
                return DateTimeTransformation.March.name
            case int(DateTimeTransformation.April.value):
                return DateTimeTransformation.April.name
            case int(DateTimeTransformation.May.value):
                return DateTimeTransformation.May.name
            case int(DateTimeTransformation.June.value):
                return DateTimeTransformation.June.name
            case int(DateTimeTransformation.July.value):
                return DateTimeTransformation.July.name
            case int(DateTimeTransformation.August.value):
                return DateTimeTransformation.August.name
            case int(DateTimeTransformation.September.value):
                return DateTimeTransformation.September.name
            case int(DateTimeTransformation.October.value):
                return DateTimeTransformation.October.name
            case int(DateTimeTransformation.November.value):
                return DateTimeTransformation.November.name
            case int(DateTimeTransformation.December.value):
                return DateTimeTransformation.December.name
