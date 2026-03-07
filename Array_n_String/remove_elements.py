from typing import List


class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        i, j = 0, 0

        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


if __name__ == '__main__':
    numbers = [0, 1, 2, 2, 3, 0, 4, 2]
    value = 2
    print(Solution().remove_element(nums=numbers, val=value))
