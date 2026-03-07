# Leet Code: 58

class Solution:
    def length_of_fast_word(self, s: str) -> int:
        length = 0
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length


if __name__ == '__main__':
    text = "luffy is still joyboy"
    print(Solution().length_of_fast_word(text))
