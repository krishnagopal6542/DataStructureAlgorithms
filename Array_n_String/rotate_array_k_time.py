# Leet Code: 189
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        # STEP:1 Reverse entire array
        reversed_array = self.reverse(nums=nums, start=0, end=len(nums) - 1)

        # STEP:2 Reverse first part of array from 0 to k-1
        reversed_first_part = self.reverse(nums=reversed_array, start=0, end=k - 1)

        # STEP:3 Reverse second part of array from k to n-1
        return self.reverse(nums=reversed_first_part, start=k, end=len(nums) - 1)

    @staticmethod
    def reverse(nums: List[int], start: int, end: int):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
        return nums


if __name__ == '__main__':
    numbers = [-1, -100, 3, 99]
    K = 2
    print(Solution().rotate(nums=numbers, k=K))
