import random as r
from common.common_assertions import CommonAssertions as common_assertions
import datetime as dt


class CommonOperatorHelper:
    """
     generate a string of random characters comprising:
     -> letters
     -> numbers
     -> symbols
    """

    @staticmethod
    def randomizer(num_of_let: int, num_of_num: int, num_of_sym: int) -> str:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u',
                   'v',
                   'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q',
                   'R',
                   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        sequence = r.sample(letters, num_of_let)
        num = r.sample(numbers, num_of_num)
        sym = r.sample(symbols, num_of_sym)

        r.shuffle(sequence)
        return ''.join([str(element) for element in sequence])

    @staticmethod
    def log_test_case_status(tc_id: bytes, tc_status: str) -> object:
        passed_status: str = "p"
        failed_status: str = "f"
        if passed_status == tc_status.lower():
            print(f"\n*****/***** Test case {tc_id} was SUCCESSFUL! *****/*****\n")
        elif failed_status == tc_status.lower():
            print(f"\n*****/***** Test case {tc_id} was UNSUCCESSFUL! *****/*****\n")
        else:
            print("Inputted test case ID or status was not valid.")

    @staticmethod
    def compare_date_n_time(greater: str, smaller: str) -> bool:

        gr_get_month: int = CommonOperatorHelper.__get_month(greater[0:3])
        sm_get_month: int = CommonOperatorHelper.__get_month(smaller[0:3])

        gr_slice_year: int = int(greater[8:12])
        gr_slice_month: int = gr_get_month
        gr_slice_date: int = int(greater[4:6])
        sm_slice_year: int = int(smaller[8:12])
        sm_slice_month: int = sm_get_month
        sm_slice_date: int = int(smaller[4:6])

        # print(f"gr_slice_year: {gr_slice_year}")
        # print(f"gr_slice_month: {gr_slice_month}")
        # print(f"gr_slice_date: {gr_slice_date}")
        #
        # print(f"sm_slice_year: {sm_slice_year}")
        # print(f"sm_slice_month: {sm_slice_month}")
        # print(f"sm_slice_date: {sm_slice_date}")

        date_time_greater = dt.datetime(gr_slice_year, gr_slice_month, gr_slice_date)
        date_time_smaller = dt.datetime(sm_slice_year, sm_slice_month, sm_slice_date)

        if date_time_greater >= date_time_smaller:
            print(f"{greater} >= {smaller}")
            return True
        else:
            print(f"{greater} <= {smaller}")
            return False

    @staticmethod
    def __get_month(month: str) -> int:
        # months are abbreviated in declaration as a dictionary
        abbr_month = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12"
        }
        if month == "Jan":
            return int(abbr_month[month])
        elif month == "Feb":
            return int(abbr_month[month])
        elif month == "Mar":
            return int(abbr_month[month])
        elif month == "Apr":
            return int(abbr_month[month])
        elif month == "May":
            return int(abbr_month[month])
        elif month == "Jun":
            return int(abbr_month[month])
        elif month == "July":
            return int(abbr_month[month])
        elif month == "Aug":
            return int(abbr_month[month])
        elif month == "Sep":
            return int(abbr_month[month])
        elif month == "Oct":
            return int(abbr_month[month])
        elif month == "Nov":
            return int(abbr_month[month])
        elif month == "Dec":
            return int(abbr_month[month])
