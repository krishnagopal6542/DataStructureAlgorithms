"""
Implement Trie DS
"""

class TrieNode:
    def __init__(self):
        self.end_of_the_word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word:str):
        crawl = self.root

        for ch in word:
            if ch not in crawl.children:
                crawl.children[ch] = TrieNode()
            crawl = crawl.children[ch]

        crawl.end_of_the_word = True

    def search(self, word:str):
        crawl = self.root

        for ch in word:
            if ch not in crawl.children:
                return False
            crawl = crawl.children[ch]

        return crawl.end_of_the_word

    def start_with(self, prefix:str):
        crawl = self.root

        for ch in prefix:
            if ch not in crawl.children:
                return False
            crawl = crawl.children[ch]

        return True


if __name__ == "__main__":
    # Initialize the Trie
    trie = Trie()

    # LeetCode 208 Example Test Case
    trie.insert("apple")
    print(trie.search("apple"))  # Returns True
    print(trie.search("app"))  # Returns False (only "apple" exists as a complete word)
    print(trie.start_with("app"))  # Returns True ("apple" has prefix "app")

    trie.insert("app")
    print(trie.search("app"))  # Returns True
