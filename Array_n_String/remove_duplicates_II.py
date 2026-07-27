"""
LeetCode: 80
Remove Duplicates from Sorted Array II
"""
from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        i, j = 2, 2
        while j < len(nums):
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i

if __name__ == '__main__':
