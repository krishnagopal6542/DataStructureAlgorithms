# Leet Code: 395

class Solution:
    def longest_substring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        # Count frequency of each character
        freq_map = {}
        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1

        # Find characters that appear less than k times
        # These characters cannot be part of valid substring
        for char, count in freq_map.items():
            if count < k:
                # Split string by this invalid character
                # and recursively find longest in each part
                max_len = 0
                for substring in s.split(char):
                    max_len = max(max_len, self.longest_substring(substring, k))
                return max_len

        # If all characters appear at least k times
        return len(s)


if __name__ == '__main__':
    STRING = "aaabb"
    K = 3
    print(Solution().longest_substring(s=STRING, k=K))
