"""
Leet Code: 214
"""

def kmp(text: str, pattern: str):
    i, j = 0, 0
    result = []
    n = len(text)
    m = len(pattern)
    lps = construct_lps(pattern=pattern)

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            result.append(i - m)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result

def construct_lps(pattern: str):
    n = len(pattern)
    lps = [0] * n

    i = 1
    length = 0

    while i < n:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    print(f"lps is {lps}")
    return lps
