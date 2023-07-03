# https://leetcode.com/problems/maximum-subarray/
# https://leetcode.com/problems/maximum-product-subarray/


class MaxSubArray:
    def __init__(self, array):
        self.array = array
        self.len = len(array)

    def max_sum(self):
        maximum_sum = self.array[0]
        cumulative_sum = self.array[0]

        for num in self.array[1:]:
            cumulative_sum = max(cumulative_sum + num, num)
            maximum_sum = max(maximum_sum, cumulative_sum)

        return maximum_sum

    def max_product(self):
        maximum_product = self.array[0]
        max_prod = self.array[0]
        min_prod = self.array[0]

        for num in self.array:
            tmp_max_prod = max(max_prod * num, max(min_prod * num, num))
            min_prod = min(min_prod * num, min(min_prod * num, num))
            max_prod = tmp_max_prod

            maximum_product = max(maximum_product, max_prod)

        return maximum_product


max_sum_arr = MaxSubArray([1, 2, -4, -7, 0, -6, 8, 10, -3])
print("Max sum subarray", max_sum_arr.max_sum())
print("Max product subarray", max_sum_arr.max_product())
