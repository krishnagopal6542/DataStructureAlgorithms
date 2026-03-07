"""
Leet Code: 3042
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
    def count_prefix_suffix_pairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0

        for j in range(n):
            prefix_trie = Trie()
            suffix_trie = Trie()

            prefix_trie.insert(words[j])
            rev_word = words[j][::-1]
            suffix_trie.insert(rev_word)

            for i in range(j):
                if len(words[i]) > len(words[j]):
                    continue

                rev = words[i][::-1]
                if prefix_trie.search(words[i]) and suffix_trie.search(rev):
                    count += 1
        return count


if __name__ == '__main__':
    word_list = ["a", "aba", "ababa", "aa"]
    print(Solution().count_prefix_suffix_pairs(words=word_list))
