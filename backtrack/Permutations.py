from typing import List, Set


class Permutations:
    def __init__(self, string: str):
        self.string: str = string

        self.length = len(string)
        self.all_permutations: Set[str] = set()

    def get_permutation(self, running_str: List[str], chars: List[str]) -> None:
        if len(running_str) == self.length:
            self.all_permutations.add("".join(running_str))
            return

        for i, c in enumerate(chars):
            running_str.append(c)
            chars.pop(i)
            self.get_permutation(running_str, chars)
            running_str.pop()
            chars.insert(i, c)

    def get_all_permutations(self) -> None:
        running_str: List[str] = []
        chars: List[str] = [c for c in self.string]

        self.get_permutation(running_str, chars)

        print(f"Number of permutations: {len(self.all_permutations)}")
        for permutation in self.all_permutations:
            print(permutation)


perms = Permutations("apple")
perms.get_all_permutations()