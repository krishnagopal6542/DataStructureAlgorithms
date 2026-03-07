# Leet Code: 28

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j, first_occurrence = 0, 0, -1
        l = len(haystack)
        if len(needle) > l:
            return -1

        while j < l:
            if haystack[j] == needle[i]:
                first_occurrence = j
                while j < l-1 and haystack[j] == needle[i]:
                    if i == len(needle) - 1:
                        return first_occurrence
                    i += 1
                    j += 1
                if i <= len(needle):
                    first_occurrence = -1
                    i = 0
            j += 1
        return first_occurrence


if __name__ == '__main__':
    haystack = "mississippi"
    needle = "issip"
    print(Solution().strStr(haystack, needle))
