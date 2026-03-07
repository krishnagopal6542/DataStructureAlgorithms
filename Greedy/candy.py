"""
Leet Code:135
"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        L2R, R2L = [1] * n, [1] * n
        total_candy = 0

        # For L2R
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                L2R[i] = max(L2R[i], L2R[i - 1] + 1)

        # For R2L
        for j in range(n - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                R2L[j] = max(R2L[j], R2L[j + 1] + 1)

        for i in range(n):
            total_candy += max(L2R[i], R2L[i])

        return total_candy

    # Optimised with Space complexity
    def candy_1(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # For L2R
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # For R2L
        for j in range(n - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candies[j] = max(candies[j], candies[j + 1] + 1)

        return sum(candies)


if __name__ == '__main__':
    rating = [1, 2, 10, 10, 10, 2, 1]
    print(Solution().candy_1(ratings=rating))
