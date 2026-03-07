# Leet Code: 127
import collections
from typing import List


class Solution:
    def ladder_length(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        if len(wordList) == 0:
            return 0

        mp = {}
        for word in wordList:
            mp[word] = False  # means this word is not visited yet

        # The endWord should be in the list
        if endWord not in mp:
            return 0

        visited = set()
        q = collections.deque()
        visited.add(begin_word)
        q.append(begin_word)

        level = 1

        while q:
            n = len(q)

            for _ in range(n):
                current_word = q.popleft()

                if current_word == end_word:
                    return level
                for i in range(len(current_word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        neighbour = current_word[:i] + ch + current_word[i + 1:]
                        if neighbour in mp and mp[neighbour] == False:
                            q.append(neighbour)
                            mp[neighbour] = True  # mark visited
            level += 1

        return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log", "cog"]
    print(Solution().ladder_length(begin_word=beginWord, end_word=endWord, word_list=wordList))
