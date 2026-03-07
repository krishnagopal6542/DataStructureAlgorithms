"""
Leet Code: 208
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:

    def __init__(self):
        """Initialize Trie data structure here."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        crawl = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if crawl.children[idx] is None:
                crawl.children[idx] = TrieNode()
            crawl = crawl.children[idx]

        crawl.end_of_world = True

    def search(self, word: str) -> bool:
        """Returns if the word is in the trie."""
        crawl = self.root

        for ch in word:
            idx = ord(ch) - ord('a')
            if crawl.children[idx] is None:
                return False
            crawl = crawl.children[idx]

        return crawl.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """Returns if there is any word in the trie that starts with the given prefix."""
        crawl = self.root

        for ch in prefix:
            idx = ord(ch) - ord('a')
            if crawl.children[idx] is None:
                return False
            crawl = crawl.children[idx]
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # True
    print(trie.search("app"))  # False
    print(trie.starts_with("app"))  # True
    trie.insert("app")
    print(trie.search("app"))  # True
