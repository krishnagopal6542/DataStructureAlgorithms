"""
Leet Code: 658
"""
from typing import List


class Solution:
    def get_index_of_x(self, arr, x):
        """ USING BINARY SEARCH """
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_element = arr[mid]

            if mid_element == x:
                return mid
            elif mid_element < x:
                left = mid + 1
            elif mid_element > x:
                right = mid - 1
        return left

    def find_closest_elements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        x_index = min(self.get_index_of_x(arr, x), n - 1)
        res = []

        left = max(0, x_index - k)
        right = min(n - 1, x_index + k)

        while right - left + 1 > k:
            if x - arr[left] <= arr[right] - x:
                right -= 1
            else:
                left += 1
        return arr[left:right + 1]

if __name__ == '__main__':
    Arr = [1, 2, 3, 4, 5]
    K = 4
    X = 3
    print(Solution().find_closest_elements(arr=Arr, k=K, x=X))