from datetime import datetime


class DateTimeHandler:
    __date_now = datetime.utcnow()

    @staticmethod
    def is_time_out(time_out: int) -> bool:
        stop: int = int(datetime.utcnow().minute) + time_out
        while datetime.utcnow().minute < stop:
            continue

        return True

    @staticmethod
    def get_minute_now() -> int:
        return DateTimeHandler.__date_now.minute

    @staticmethod
    def get_second_now() -> int:
        return DateTimeHandler.__date_now.second

    @staticmethod
    def get_hour_now() -> int:
        return DateTimeHandler.__date_now.hour


print(datetime.now().isoweekday())
