"""
Leet Code: 151
"""

def reverse_words(s: str):
    s = list(s)
    s.reverse()

    i, l, r = 0, 0, 0
    n = len(s)

    while i < n:
        while i < n and s[i] != ' ':
            s[r] = s[i]
            r += 1
            i += 1
        if l < r:
            s[l:r] = reversed(s[l:r])

            if r < n:
                s[r] = ' '
                r += 1

            l = r
        i += 1
    s = ''.join(s)
    return s


if __name__ == '__main__':
    strings = "  hello world  "
    print(reverse_words(strings))
