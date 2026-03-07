# https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1
class Solution:
    def longest_substring(self, s: str, k: int) -> int:
        i, j = 0, 0
        freq_map = {}
        max_sub_string_length = 0

        while j < len(s):
            freq_map[s[j]] = freq_map.get(s[j], 0) + 1
            if len(freq_map) == k:
                sub_string_len = j - i + 1
                max_sub_string_length = max(max_sub_string_length, sub_string_len)
            else:
                while len(freq_map) > k:
                    freq_map[s[i]] -= 1
                    if freq_map[s[i]] == 0:
                        del freq_map[s[i]]
                    i += 1
            j += 1
        return max_sub_string_length


if __name__ == '__main__':
    STRING = "pwwkew"
    K = 3
    print(Solution().longest_substring(s=STRING, k=K))
