# Leet Code: 26
from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        i, j = 0, 1

        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        print(nums)
        return i + 1


if __name__ == '__main__':
    numbers = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().remove_duplicates(nums=numbers))
