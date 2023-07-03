from typing import List, Optional


class RotateByK:
    def __init__(self, nums: List[int], k: int):
        self.nums: List[int] = nums
        self.k: int = k

        self.length: int = len(nums)

        if k > self.length:
            self.k = self.k % self.length

    def rotate_array(self):
        start_idx: int = 0
        curr_idx: int = 0
        next_idx: int = 0
        curr_val: int = 0
        next_val: int = 0
        num_swaps: int = 0

        while start_idx < self.length and num_swaps < self.length:
            curr_idx = start_idx
            curr_val = self.nums[curr_idx]

            while num_swaps < self.length:
                next_idx = (curr_idx + self.k) % self.length
                next_val = self.nums[next_idx]

                self.nums[next_idx] = curr_val
                curr_val = next_val
                curr_idx = next_idx
                num_swaps += 1
                if curr_idx == start_idx:
                    break

            start_idx += 1


rotate = RotateByK([1, 2, 3, 4, 5, 6, 7], 3)
rotate.rotate_array()
print(rotate.nums)
