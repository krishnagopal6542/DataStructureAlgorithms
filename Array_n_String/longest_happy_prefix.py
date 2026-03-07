"""
Leet Code: 1392
Approach: Implementing LPS of KMP algorithm
"""


def compute_lps(pattern: str):
    n = len(pattern)
    LPS = [0] * n

    length = 0
    i = 1

    while i < n:
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
    print("LPS ==> ", LPS)
    return LPS


def longest_prefix(s: str):
    lps = compute_lps(pattern=s)

    # The last value in LPS array gives the length of longest prefix-suffix
    longest_len = lps[-1]
    return s[0:longest_len]


if __name__ == '__main__':
    txt = "level"
    print(longest_prefix(s=txt))
