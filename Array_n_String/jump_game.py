# Leet Code: 55
from typing import List


class Solution:
    def can_jump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True


if __name__ == '__main__':
    numbers = [3, 2, 1, 1, 4]
    print(Solution().can_jump(nums=numbers))
