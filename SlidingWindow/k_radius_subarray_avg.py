"""
Leet Code: 2090
"""

from typing import List


class Solution:
    def get_averages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        i, j = 0, 0
        final_average = [-1] * n
        window = k * 2 + 1  # as k is radius , so window length will be twice of k
        window_sum = 0
        while j < n:
            window_sum += nums[j]
            if j - i + 1 == window:
                avg = window_sum // window
                # Center of window: k elements back from right edge
                centre_index = j - k
                final_average[centre_index] = avg
                window_sum = window_sum - nums[i]
                i += 1
            j += 1
        return final_average


if __name__ == '__main__':
    number = [7, 4, 3, 9, 1, 8, 5, 2, 6]
    K = 3
    print(Solution().get_averages(nums=number, k=K))
