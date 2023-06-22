from datetime import datetime


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
