class Solution:

    def get_lps(self, pattern: str):
        """
        Create a LPS array to store the length of longest proper prefix which is also a sufix.
        LPS[i] is:
            * The longest proper prefix of pattern[0....i]
            * Which is also a suffix of pattern[0.....i]
        """
        m = len(pattern)
        LPS = [0] * m

        length, i = 0, 1

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                LPS[i] = length
                i += 1
            else:
                if length != 0:
                    length = LPS[length - 1]
                else:
                    LPS[i] = 0
                    i += 1

        return LPS


    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0
        n = len(haystack)
        m = len(needle)
        if n < m:
            return -1
        lps = self.get_lps(pattern=needle)

        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == m:
                first_index_occurrence = i - m
                return first_index_occurrence
            elif needle[j] != haystack[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1
