"""
Leet Code: 859
"""


class Solution:
    def check_freq(self, s):
        # Array to store frequency of each character (a-z)
        arr = [0] * 26

        for ch in s:
            arr[ord(ch) - ord('a')] += 1

            if arr[ord(ch) - ord('a')] > 1:
                return True

        return False

    def buddy_strings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            return self.check_freq(s)

        return False


if __name__ == '__main__':
    inp_str = "ab"
    goal_str = "ba"
    print(Solution().buddy_strings(s=inp_str, goal=goal_str))
