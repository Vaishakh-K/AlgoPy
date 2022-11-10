class NoThreeConsecutive:
    def __init__(self, s: str):
        self.str = s

        self.length = len(s)

    def get_minimum_moves(self) -> int:
        num_moves: int = 0

        if self.length < 2:
            return 0

        prev_char: str = self.str[0]
        count: int = 1

        for i in range(1, self.length):
            curr_char = self.str[i]
            if curr_char == prev_char:
                count += 1
            else:
                num_moves += count // 3
                count = 1
                prev_char = curr_char

        return num_moves


no_three_cons = NoThreeConsecutive("aaaaaabaaaaabbbba")
print(no_three_cons.get_minimum_moves())
