"""
LC : 1431. Kids With the Greatest Number of Candies
"""
from typing import List


class Solution:
    def kids_with_candies(self, candies: List[int], extra_candies: int) -> List[bool]:
        max_val = max(candies)
        res = [False] * len(candies)

        for i in range(len(candies)):
            if candies[i] + extra_candies >= max_val:
                res[i] =True
            else:
                res[i] = False
        return res


if __name__ == '__main__':
    Candies = [2, 3, 5, 1, 3]
    ExtraCandies = 3
    print(Solution().kids_with_candies(candies=Candies, extra_candies=ExtraCandies))
