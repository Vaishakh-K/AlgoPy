from typing import List, Dict
import heapq
from collections import Counter


class KMostFrequent:
    def __init__(self, nums: List[int], k: int):
        self.nums: List[int] = nums
        self.k: int = k

        self.length: int = len(self.nums)

    def find_k_most_frequent(self):
        count_map: Dict[int, int] = Counter(self.nums)

        return heapq.nlargest(self.k, count_map, key=lambda x: count_map.get(x))


km = KMostFrequent([1, 3, 4, 2, 2, 1, 6, 1, 1, 1, 6, 6, 2, 3, 6], 2)
print(km.find_k_most_frequent())
