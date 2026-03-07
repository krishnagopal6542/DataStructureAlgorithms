"""
Leet Code: 3043
"""
from typing import List


class TrieNode:
    def __init__(self):
        self.children = [None] * 25


class Solution:
    def insert(self, root, num: str):
        crawl = root
        for ch in num:
            idx = int(ch)
            if not crawl.children[idx]:
                crawl.children[idx] = TrieNode()
            crawl = crawl.children[idx]

    def search(self, root, num):
        crawl = root
        num_str = str(num)
        length = 0
        for ch in num_str:
            idx = int(ch)
            if crawl.children[idx]:
                length += 1
                crawl = crawl.children[idx]
            else:
                break
        return length

    def longest_common_prefix(self, arr1: List[int], arr2: List[int]) -> int:
        root = TrieNode()
        # Build Trie
        for num in arr1:
            self.insert(root, str(num))

        result = 0
        for num in arr2:
            result = max(result, self.search(root, num))

        return result


if __name__ == '__main__':
    arr_1 = [1, 10, 100]
    arr_2 = [1000]
    print(Solution().longest_common_prefix(arr1=arr_1, arr2=arr_2))
