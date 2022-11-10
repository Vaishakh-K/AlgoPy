from typing import List


class TwoSum:
    def __init__(self, array: List[int], target: int):
        self.array: List[int] = array
        self.target: int = target

        self.length: int = len(array)
        list.sort(self.array)

    def get_2sum(self) -> List[List[int]]:
        start: int = 0
        end: int = self.length - 1

        list_2sum: List[List[int]] = []
        while start < end < self.length:
            curr_sum = self.array[start] + self.array[end]
            if curr_sum == self.target:
                list_2sum.append([self.array[start], self.array[end]])
                start += 1
                end -= 1
            elif curr_sum < self.target:
                start += 1
            else:
                end -= 1

        return list_2sum


array = [1, 0, -1, 1, 0, -2, 2]
target = 0
two_sum = TwoSum(array, target)
result = two_sum.get_2sum()
for item in result:
    print(item)
