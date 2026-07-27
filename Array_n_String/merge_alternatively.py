class Solution:
    @staticmethod
    def merge_alternately(word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i = 0
        res = []

        while i < m and i < n:
            res.append(word1[i])
            res.append(word2[i])
            i += 1

        return "".join(res) + word1[i:] + word2[i:]

if __name__ == '__main__':
    word_1 = "abcd"
    word_2 = "pq"
    print(Solution().merge_alternately(word1=word_1, word2=word_2))
