"""
Topic: Sliding Window
Problem: https://www.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1
"""

# Brute Force Approach
# def main(text: str, pattern: str) -> int:
#     k = len(pattern)
#     i, j = 0, 0
#     count = 0
#
#     sorted_pattern = ''.join(sorted(pattern))
#
#     sub_text = ''
#     while j < len(text):
#         sub_text += text[j]
#         if j - i + 1 < k:
#             j += 1
#         elif j - i + 1 == k:
#             sorted_sub_text = ''.join(sorted(sub_text))
#             if sorted_pattern == sorted_sub_text:
#                 count += 1
#             sub_text = sub_text[1:]
#             i += 1
#             j += 1
#     return count


def main(text: str, pattern: str) -> int:
    k = len(pattern)
    i, j, ans = 0, 0, 0
    mp = {}

    for element in pattern:
        mp[element] = mp.get(element, 0) + 1
    count = len(mp)

    while j < len(text):
        if text[j] in mp:
            mp[text[j]] -= 1
            if mp[text[j]] == 0:
                count -= 1
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            if count == 0:
                ans += 1
            if text[i] in mp:
                mp[text[i]] += 1
                if mp[text[i]] == 1:
                    count += 1
            i += 1
            j += 1
    return ans


if __name__ == '__main__':
    txt = "aabaabaa"
    pat = "aaba"
    print(main(text=txt, pattern=pat))
