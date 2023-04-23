import random as r
from common.common_assertions import CommonAssertions as common_assertions


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
        pass_status: str = "p"
        failed_status: str = "f"
        if common_assertions.verify_string_is_equal(exp_str=pass_status,
                                                    act_str=tc_status.lower()):
            print(f"\n*****/***** Test case {tc_id} was SUCCESSFUL! *****/*****\n")
        elif common_assertions.verify_string_is_equal(exp_str=failed_status,
                                                      act_str=tc_status.lower()):
            print(f"\n*****/***** Test case {tc_id} was UNSUCCESSFUL! *****/*****\n")
        else:
            print("Inputted test case ID or status was not valid.")
