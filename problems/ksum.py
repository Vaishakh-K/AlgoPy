from typing import List, Optional


class KSum:
    def __init__(self, array: List[int], target: int):
        self.array: List[int] = array
        self.target: int = target

        list.sort(self.array)
        self.length: int = len(self.array)
        self.result_list: List[List[int]] = []

    def two_sum(self, s: int, e: int, target_sum: int, curr_list: List[int]) -> None:
        start: int = s
        end: int = self.length - 1

        while start < end:
            curr_sum: int = self.array[start] + self.array[end]
            if curr_sum == target_sum:
                curr_list.append(self.array[start])
                curr_list.append(self.array[end])

                tmp_list = List.copy(curr_list)
                self.result_list.append(tmp_list)

                curr_list.remove(self.array[start])
                curr_list.remove(self.array[end])
                end -= 1
                start += 1
                while start < self.length and self.array[start] == self.array[start - 1]:
                    start += 1
            elif curr_sum > target_sum:
                end -= 1
            else:
                start += 1

    def get_nums_summing_to_target(self, s: int, target_sum: int, k: int, curr_list: List[int]) -> None:
        if k == 2:
            return self.two_sum(s, self.length - 1, target_sum, curr_list)

        while s < self.length:
            curr_list.append(self.array[s])
            self.get_nums_summing_to_target(s + 1, target_sum - self.array[s], k - 1, curr_list)
            curr_list.remove(self.array[s])
            s += 1
            while s < self.length and self.array[s] == self.array[s - 1]:
                s += 1


array = [1, 0, -1, 0, -2, 2]
target = 0
k = 4
ksum = KSum(array, target)
ksum.get_nums_summing_to_target(0, ksum.target, k, [])

for item in ksum.result_list:
    print(item)
