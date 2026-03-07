"""
Leet Code: 14
"""
from typing import List


def longest_common_prefix(strings: List[str]):
    strings.sort()

    # First and last elements of list
    first, last = strings[0], strings[-1]

    result = ''
    for i in range(len(first)):
        if first[i] != last[i]:
            break
        result += first[i]
    return result


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(longest_common_prefix(strings=strs))
