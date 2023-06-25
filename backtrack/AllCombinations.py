# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# Link: https://leetcode.com/problems/combinations/description/
import copy
from typing import List


class Combinations:
    def __init__(self):
        self.combinations: List[List[int]] = []
        self.k = None
        self.n = None
        self.nums = None

    def construct_combinations(self, list_so_far: List[int], rem_list: List[int]):
        if len(list_so_far) == self.k:
            self.combinations.append(copy.deepcopy(list_so_far))
        else:
            for i in range(len(rem_list)):
                list_so_far.append(rem_list[i])
                self.construct_combinations(list_so_far, rem_list[i+1:])
                list_so_far.pop()

    def get_combinations(self, n, k):
        self.combinations: List[List[int]] = []
        self.k = k
        self.n = n
        nums = list(range(1, n + 1))

        self.construct_combinations([], nums)
        return self.combinations


combinations = Combinations()
all_combinations = combinations.get_combinations(4, 2)

print(f"nCk combinations", all_combinations)
