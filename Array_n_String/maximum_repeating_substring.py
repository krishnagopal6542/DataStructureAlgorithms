# Leet Code: 1668

def compute_lps(pattern: str):
    n = len(pattern)
    LPS = [0] * n
    length, i = 0, 1

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
    return LPS


def kmp_algorithm(text: str, pattern: str):
    lps = compute_lps(pattern)
    n = len(text)
    m = len(pattern)
    result = []
    i, j = 0, 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            return True
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False


def max_repeating(text: str, pattern: str) -> int:
    max_k = 0
    k = 1

    while kmp_algorithm(text=text, pattern=pattern):
        max_k = k
        k += 1
    return max_k


if __name__ == '__main__':
    sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
    word = "aaaba"
    print(max_repeating(text=sequence, pattern=word))
