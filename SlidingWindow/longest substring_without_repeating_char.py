# Leetcode: 904

class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        i, j = 0, 0
        freq_map = {}
        max_substring_len = 0

        while j < len(s):
            freq_map[s[j]] = freq_map.get(s[j], 0) + 1
            if len(freq_map) == j - i + 1:
                max_substring_len = max(max_substring_len, j - i + 1)
            elif len(freq_map) < j - i + 1:
                while len(freq_map) < j - i + 1:
                    freq_map[s[i]] -= 1
                    if freq_map[s[i]] == 0:
                        del freq_map[s[i]]
                    i += 1
            j += 1
        return max_substring_len


if __name__ == '__main__':
    STRING = 'pwwkew'
    print(Solution().length_of_longest_substring(s=STRING))
