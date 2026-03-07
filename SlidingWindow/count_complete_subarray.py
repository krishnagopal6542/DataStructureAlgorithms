"""
Leet Code: 2799
"""
from typing import List


class Solution:
    def count_complete_subarrays(self, nums: List[int]) -> int:
        n = len(nums)
        unique_map = {}
        window_map = {}
        i, j = 0, 0
        count = 0

        for k, num in enumerate(nums):
            unique_map[num] = 1 + unique_map.get(num, 0)

        unique_element = len(unique_map)

        while j < n:
            window_map[nums[j]] = 1 + window_map.get(nums[j], 0)
            while len(window_map) == unique_element:
                count += n - j
                window_map[nums[i]] -= 1
                if window_map[nums[i]] == 0:
                    del window_map[nums[i]]
                i += 1
            j += 1
        return count


if __name__ == '__main__':
    number = [1, 3, 1, 2, 2]
    print(Solution().count_complete_subarrays(nums=number))
