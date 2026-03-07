"""
Leet Code: 2416
"""
from itertools import count
from typing import List


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0


class Solution:
    def insert(self, root, word) -> None:
        crawl = root

        for ch in word:
            idx = ord(ch) - ord('a')
            if crawl.children[idx] is None:
                crawl.children[idx] = TrieNode()
            crawl.children[idx].count += 1
            crawl = crawl.children[idx]

    def get_score(self, root, word):
        crawl = root
        score = 0

        for ch in word:
            idx = ord(ch) - ord('a')
            score += crawl.children[idx].count
            crawl = crawl.children[idx]
        return score

    def sum_prefix_scores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        n = len(words)
        result = [0] * n

        # Build Trie
        for word in words:
            self.insert(root, word)

        for i in range(n):
            result[i] = self.get_score(root, words[i])

        return result


if __name__ == '__main__':
    word_list = ["abc", "ab", "bc", "b"]
    print(Solution().sum_prefix_scores(words=word_list))
