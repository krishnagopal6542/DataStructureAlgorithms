# Leet Code: 686

def compute_lps(pattern: str):
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


def kmp_algorithm(text: str, pattern: str):
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)

    i, j = 0, 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            return i - j  # Match found
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1  # No Match found


def repeated_string_match(a: str, b: str) -> int:
    m = len(a)
    n = len(b)
    len_to_add = n - 1
    j = 0

    # Make a
    for i in range(len_to_add):
        ch = a[j]
        a += ch
        j = (j + 1) % m

    # checking for first occurrence
    starting_index = kmp_algorithm(text=a, pattern=b)

    # getting the no. of times a was actually used
    ans = -1
    if starting_index != -1:
        used_len_for_string_A = starting_index + n
        ans = used_len_for_string_A // m
        if used_len_for_string_A % m:
            ans += 1

    return ans


if __name__ == '__main__':
    _a = "abcd"
    _b = "cdabcdab"
    print(repeated_string_match(a=_a, b=_b))
