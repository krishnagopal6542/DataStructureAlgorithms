"""
Leet Code: 648
"""
from typing import List


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        crawl = self.root

        for ch in word:
            idx = ord(ch) - ord('a')
            if crawl.children[idx] is None:
                crawl.children[idx] = TrieNode()
            crawl = crawl.children[idx]
        crawl.end_of_word = True

    def search(self, word:str):
        crawl = self.root

        for i, ch in enumerate(word):
            idx = ord(ch) - ord('a')
            if crawl.children[idx] is None:
                return word

            crawl = crawl.children[idx]
            if crawl.end_of_word:
                return word[:i+1]

        return word


    def replace_words(self, dictionary: List[str], sentence: str) -> str:
        self.root = TrieNode()

        # Build Trie
        for word in dictionary:
            self.insert(word)

        words = sentence.split(' ')
        result = []

        for word in words:
            result.append(self.search(word))

        return ' '.join(result)

if __name__ == '__main__':
    _dictionary = ["cat", "bat", "rat"]
    _sentence = "the cattle was rattled by the battery"
    print(Solution().replace_words(dictionary=_dictionary, sentence=_sentence))