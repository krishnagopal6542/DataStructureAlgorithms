from typing import List


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = 0

        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                if current_sum > max_sum:
                    max_sum = current_sum
        return max_sum


if __name__ == '__main__':
    number = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().max_sub_array(nums=number))
