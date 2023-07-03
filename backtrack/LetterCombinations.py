from typing import List


class LetterCombinations:
    def __init__(self, digits: str):
        self.digits = digits
        self.map = dict()
        self.target_len = len(digits)
        self.all_combinations: List[str] = []

    def get_combinations(self, digits_list: List[str], curr_string: List[str]) -> None:
        if len(curr_string) == self.target_len:
            string: str = "".join(curr_string)
            self.all_combinations.append(string)
        else:
            curr_digit = digits_list[0]

            for char in self.map[curr_digit]:
                curr_string.append(char)
                self.get_combinations(digits_list[1:], curr_string)
                curr_string.pop(-1)

    def get_all_letter_combinations(self) -> List[str]:
        if self.target_len < 1:
            return self.all_combinations

        all_digits = "23456789"
        chars = "abcdefghijklmnopqrstuvwxyz"

        char_idx = 0
        for digit in all_digits:
            if digit == "7" or digit == "9":
                self.map[digit] = [c for c in chars[char_idx : char_idx + 4]]
                char_idx += 4
            else:
                self.map[digit] = [c for c in chars[char_idx : char_idx + 3]]
                char_idx += 3

        curr_string = []
        digits_list = [c for c in self.digits]
        self.get_combinations(digits_list, curr_string)

        return self.all_combinations


all_combs = LetterCombinations("27")
combs = all_combs.get_all_letter_combinations()

print(f"Number of combinations: {len(combs)}")
for comb in combs:
    print(comb)
