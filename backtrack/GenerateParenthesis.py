from typing import List


class GenerateParenthesis:
    def __init__(self, n):
        self.n = n

        self.all_parenthesis: List[str] = []

    def construct_valid_parenthesis(self, string: str, remaining_open: int, closed_so_far: int) -> None:
        if remaining_open == 0 and closed_so_far == self.n:
            self.all_parenthesis.append(string)
            return

        if remaining_open > 0:
            string += "("
            self.construct_valid_parenthesis(string, remaining_open - 1, closed_so_far)
            string = string[:-1]

        if closed_so_far < self.n - remaining_open:
            string += ")"
            self.construct_valid_parenthesis(string, remaining_open, closed_so_far + 1)
            string = string[:-1]

    def generate_parenthesis(self):
        self.construct_valid_parenthesis("", self.n, 0)

        print(f"Number of valid parentheses: {len(self.all_parenthesis)}")
        for parenthesis in self.all_parenthesis:
            print(parenthesis)


parenthesis = GenerateParenthesis(4)
parenthesis.generate_parenthesis()


