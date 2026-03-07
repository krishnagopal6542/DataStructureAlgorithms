"""
Topic: Sliding Window
Problem: https://leetcode.com/problems/sliding-subarray-beauty/description/?envType=problem-list-v2&envId=vitgfaa2
"""
from typing import List


def main(nums: List, k: int, x: int) -> List[int]:
    i, j = 0, 0
    result = []
    freq = [0] * 51

    while j < len(nums):
        if nums[j] < 0:
            freq[abs(nums[j])] += 1
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            beauty = 0
            count = 0
            for val in range(50, 0, -1):  # Most negative to least negative
                count += freq[val]
                if count >= x:
                    beauty = -val
                    break
            result.append(beauty)

            # Remove outgoing element
            if nums[i] < 0:
                freq[abs(nums[i])] -= 1
            i += 1
            j += 1
    return result


if __name__ == '__main__':
    array = [1, -1, -3, -2, 3]
    K = 3
    X = 2
    print(main(nums=array, k=K, x=X))
