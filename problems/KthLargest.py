from typing import List
import queue
import heapq


class KthLargest:
    def __init__(self, nums: List[int], k: int):
        self.nums: List[int] = nums
        self.k: int = k

        self.length: int = len(self.nums)

    def get_k_largest(self) -> int:
        pq = queue.PriorityQueue(self.k)
        for num in self.nums:
            if not pq.full():
                pq.put(num)
            else:
                least_elem = pq.get()
                if least_elem > num:
                    pq.put(least_elem)
                else:
                    pq.put(num)

        return pq.get()

        # # Alternate is to use heapq
        # return heapq.nlargest(self.k, self.nums, key=lambda x: x)[-1]


kth_largerst = KthLargest([4, 6, 1, 9, 2, 10], 3)
print(kth_largerst.get_k_largest())
