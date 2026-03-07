"""
    YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=qases-9gOpk
    Company Tags                : MICROSOFT
    GfG Link                    : https://www.geeksforgeeks.org/problems/search-pattern0205/1
"""

"""
    Approach-1 (Brute Force) 
    Simply try with every possible index at i and iterate on pattern and keep trying.
    T.C : O(m*n)
    S.C : O(1)
    
    Approach-2 (KMP Algorithm)
    T.C : O(m+n)
    S.C : O(m) where m is the length of pattern
"""


def kmp(text: str, pattern: str):
    i, j = 0, 0
    result = []
    n = len(text)
    m = len(pattern)
    lps = get_lps(pattern=pattern)

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


def get_lps(pattern: str):
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
    print("LPS ==>", LPS)

    return LPS


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


if __name__ == '__main__':
    _text = 'leetcode'
    _pattern = 'aaacaaaa'
    print(kmp(text=_text, pattern=_pattern))
    print(construct_lps(pattern=_pattern))
