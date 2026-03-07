# Leet Code: 122
from typing import List


class Solution:
    def max_profit(self, prices: List[int]):
        min_val, max_val = float('inf'), 0
        profit_sum = 0

        for price in prices:
            min_val = min(min_val, price)
            profit = price - min_val
            if profit > max_val:
                profit_sum += profit
                min_val, max_val = float('inf'), 0

        return max_val, profit_sum


if __name__ == '__main__':
    Prices = [1, 2, 3, 4]
    print(Solution().max_profit(prices=Prices))
