"""
Topic: Sliding Window
Problem: https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1
"""
import collections
from typing import List


def main(array_list: List, k: int) -> List[int]:
    i, j = 0, 0
    q = []
    result = []

    while j < len(array_list):
        if array_list[j] < 0:
            q.append(array_list[j])
        if j - i + 1 == k:
            if len(q) == 0:
                result.append(0)
            else:
                result.append(q[0])
                if array_list[i] == q[0]:
                    q.pop(0)
            i += 1
        j += 1
    return result


def main_using_deque(array_list: List, k: int) -> List[int]:
    i, j = 0, 0
    q = collections.deque()
    result = []

    while j < len(array_list):
        if array_list[j] < 0:
            q.append(array_list[j])
        if j - i + 1 == k:
            if not q:
                result.append(0)
            else:
                negative_value = q[0]
                result.append(negative_value)
                if array_list[i] < 0:
                    q.popleft()
            i += 1
        j += 1
    return result


if __name__ == '__main__':
    arr = [12, -1, -7, 8, -15, 30, 16, 28]
    window_size = 3
    print(main(array_list=arr, k=window_size))
    # print(main_using_dequeg_deque(array_list=arr, k=window_size))
