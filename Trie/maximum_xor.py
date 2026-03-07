"""
Leet Code: 421
"""
from typing import List


class TrieNode:
    def __init__(self):
        self.left = None
        self.right = None


class Solution:

    def insert(self, root, num):
        crawl = root
        for i in range(31, -1, -1):
            ith_bit = (num >> i) & 1
            if ith_bit == 0:
                if crawl.left is None:
                    crawl.left = TrieNode()
                crawl = crawl.left
            else:
                if crawl.right is None:
                    crawl.right = TrieNode()
                crawl = crawl.right

    def max_xor(self, root, num):
        _max_xor = 0
        crawl = root
        """
        Moving from left most bit(MSB) to right most(LSB) to get max answer
        to get set bit 1 in left most position (MSB) to get large decimal value
        """
        for i in range(31, -1, -1):
            ith_bit = (num >> i) & 1
            # I want maximum one in my result of xor
            # so, if I have current bit of 'num' = 1, I will select path where I get 0 in some other number
            if ith_bit == 1:
                if crawl.left:
                    _max_xor += (1 << i)  # if I am able to go to left, I can get 1 as XOR result
                    crawl = crawl.left
                else:
                    crawl = crawl.right
            else:
                if crawl.right:
                    _max_xor += (1 << i)  # if I am able to go to right, I can get 1 as XOR result
                    crawl = crawl.right
                else:
                    crawl = crawl.left

        return _max_xor

    def find_maximum_xor(self, nums: List[int]) -> int:
        root = TrieNode()
        # Build Trie for nums
        for num in nums:
            self.insert(root, num)

        # Calculate maximum XOR of two numbers
        result = 0
        for num in nums:
            temp = self.max_xor(root, num)
            result = max(result, temp)

        return result


if __name__ == '__main__':
    inp_nums = [3, 10, 5, 25, 2, 8]
    print(Solution().find_maximum_xor(nums=inp_nums))
