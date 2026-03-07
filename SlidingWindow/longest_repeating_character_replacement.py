# Leet Code: 424

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j = 0, 0
        char_freq = {}
        result = 0
        max_freq = 0

        while j < len(s):
            char_freq[s[j]] = char_freq.get(s[j], 0) + 1
            max_freq = max(max_freq, char_freq[s[j]])

            while (j - i + 1) - max_freq > k:
                char_freq[s[i]] -= 1
                if char_freq[s[i]] == 0:
                    del char_freq[s[i]]
                i += 1
            result = max(result, j - i + 1)
            j += 1
        return result


if __name__ == '__main__':
    STRING = "ABAB"
    K = 2
    print(Solution().characterReplacement(s=STRING, k=K))
