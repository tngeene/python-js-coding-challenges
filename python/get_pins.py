import itertools
from typing import List


# original challenge from https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

combos = {
    "1": ["1", "2", "4"],
    "2": ["2", "1", "3", "5"],
    "3": ["3", "2", "6"],
    "4": ["4", "1", "5", "7"],
    "5": ["5", "2", "4", "6", "8"],
    "6": ["6", "3", "5", "9"],
    "7": ["7", "4", "8"],
    "8": ["8", "0", "5", "7", "9"],
    "9": ["9", "6", "8"],
    "0": ["0", "8"],
}

def get_pins(observed: List[str]) -> List[str]:
    # we get the possible combos by getting the index of each observed digit
    # and retrieve the value from the combo dict.
    possible_combos = [combos[number] for number in observed]
    # generate every permutation of the possible numbers
    return ([''.join(combo) for combo in itertools.product(*possible_combos)])

if __name__ == "__main__":
    # example data, feel free to change
    get_pins(['8', '2', '4', '7'])
