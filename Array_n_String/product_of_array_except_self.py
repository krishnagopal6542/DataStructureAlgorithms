# Leet Code: 238
from typing import List


class Solution:
    def product_except_self_1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count_zero = 0
        prd_without_zero = 1

        for num in nums:
            if num == 0:
                count_zero += 1
            else:
                prd_without_zero *= num

        res = [1] * n
        for i in range(n):
            if nums[i] != 0:
                if count_zero > 0:
                    res[i] = 0
                else:
                    res[i] = int(prd_without_zero / nums[i])
            else:
                if count_zero > 1:
                    res[i] = 0
                else:
                    res[i] = prd_without_zero

        return res

    def product_except_self_4(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


if __name__ == '__main__':
    numbers = [1, 2, 3, 4]
    print(Solution().product_except_self_1(nums=numbers))
