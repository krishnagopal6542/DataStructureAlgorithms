"""
Leet Code: 713
"""

from typing import List


class Solution:
    def num_subarray_product_less_than_k(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        n = len(nums)
        i, j = 0, 0
        product = 1
        total_possible_subarray = 0

        while j < n:
            product *= nums[j]
            while product >= k:
                product = product / nums[i]
                i += 1
            total_possible_subarray += j - i + 1
            j += 1
        return total_possible_subarray


if __name__ == '__main__':
    numbers = [10,5,2,6]
    K = 100
    print(Solution().num_subarray_product_less_than_k(nums=numbers, k=K))
