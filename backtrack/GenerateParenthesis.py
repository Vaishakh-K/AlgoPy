from typing import List


class GenerateParenthesis:
    def __init__(self, n):
        self.n = n

        self.all_parenthesis: List[str] = []

    def construct_well_formed_parenthesis(
        self, paren_str: str, num_open: int, num_closed: int
    ):
        if num_open == self.n and num_closed == self.n:
            self.all_parenthesis.append(paren_str)

        if num_open < self.n:
            paren_str += "("
            self.construct_well_formed_parenthesis(paren_str, num_open + 1, num_closed)
            paren_str = paren_str[:-1]

        if num_closed < num_open:
            paren_str += ")"
            self.construct_well_formed_parenthesis(paren_str, num_open, num_closed + 1)
            paren_str = paren_str[:-1]

    def generate_parenthesis(self):
        self.construct_well_formed_parenthesis("", 0, 0)

        print(f"Number of valid parentheses: {len(self.all_parenthesis)}")
        for parenthesis in self.all_parenthesis:
            print(parenthesis)


parenthesis = GenerateParenthesis(4)
parenthesis.generate_parenthesis()
