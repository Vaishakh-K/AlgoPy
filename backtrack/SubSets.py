from typing import List, Optional


class SubSets:
    def __init__(self, digits: List[int]):
        self.digits: List[int] = digits

        self.length = len(digits)
        self.all_subsets: List[List[int]] = []

    def get_subset(self, subset: List[int], start: int):
        self.all_subsets.append(list.copy(subset))

        for i in range(start, self.length):
            subset.append(self.digits[i])
            self.get_subset(subset, i + 1)
            subset.pop()

    def get_all_subsets(self):
        init_subset: List[int] = []
        start: int = 0

        self.get_subset(init_subset, start)

        print(f"Number of subsets: {len(self.all_subsets)}")
        for subset in self.all_subsets:
            print(subset)


subsets = SubSets([1, 2, 3])
subsets.get_all_subsets()