def count_anagram_occurrence(txt, pat):
    pat_map = {}
    for ch in pat:
        pat_map[ch] = 1 + pat_map.get(ch, 0)
    window_map = {}

    k = len(pat)
    i, j = 0, 0
    count = 0

    while j < len(txt):
        window_map[txt[j]] = 1 + window_map.get(txt[j], 0)
        if j - i + 1 == k:
            if window_map == pat_map:
                count += 1
            window_map[txt[i]] -= 1
            if window_map[txt[i]] == 0:
                del window_map[txt[i]]
            i += 1
        j += 1

    return count


if __name__ == '__main__':
    txt = "aabaabaa"
    pat = "aaba"
    print(count_anagram_occurrence(txt, pat))
