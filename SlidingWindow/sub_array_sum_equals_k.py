# Leet Code: 506
from typing import List


class Solution:
    def subarray_sum(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        count = 0
        array_sum = 0
        sum_map = {0: 1}

        for num in nums:
            array_sum += num
            if array_sum - k in sum_map:
                count += sum_map[array_sum - k]
            sum_map[array_sum] = sum_map.get(array_sum, 0) + 1

        return count


if __name__ == '__main__':
    array_list = [-1, -1, 1]
    K = 0
    print(Solution().subarray_sum(nums=array_list, k=K))
