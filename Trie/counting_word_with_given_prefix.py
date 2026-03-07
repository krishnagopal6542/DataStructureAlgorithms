"""
Leet Code: 2185
"""
from typing import List


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        crawl = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if crawl.children[idx] is None:
                crawl.children[idx] = TrieNode()
            crawl = crawl.children[idx]
        crawl.end_of_word = True

    def search(self, word):
        crawl = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if crawl.children[idx] is None:
                return False
            crawl = crawl.children[idx]
        return True


class Solution:
    def prefix_count(self, words: List[str], pref: str) -> int:
        n = len(words)
        count = 0

        for word in words:
            root = Trie()
            root.insert(word)
            if root.search(pref):
                count += 1
        return count


if __name__ == '__main__':
    word_list = ["pay", "attention", "practice", "attend"]
    prefix_char = "at"
    print(Solution().prefix_count(words=word_list, pref=prefix_char))
