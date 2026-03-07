"""
    YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=qases-9gOpk
    Company Tags                : MICROSOFT
    LEET CODE                 : 1408
"""


def kmp_algorithm(text: str, pattern: str):
    lps = pattern_lps(pattern)
    i, j = 0, 0
    n, m = len(text), len(pattern)

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            return pattern
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return None


def pattern_lps(pattern: str):
    m = len(pattern)
    LPS = [0] * m
    length, i = 0, 1  # LPS of index 0 is always 0, so i start from 1

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


def string_matching_driver(string_array):
    result = set()
    n = len(string_array)
    for i in range(n):
        txt = string_array[i]
        for j in range(len(string_array)):
            if i != j:
                pattern = string_array[j]
                if len(pattern) <= len(txt):
                    response = kmp_algorithm(text=txt, pattern=pattern)
                    if response:
                        result.add(response)
    return list(result)


if __name__ == '__main__':
    words = ["leetcoder","leetcode","od","hamlet","am"]
    print(string_matching_driver(string_array=words))
