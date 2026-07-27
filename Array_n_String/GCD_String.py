"""
Leet Code: 1071
Greatest Common Divisor of Strings
"""
import math
class Solution:
    @staticmethod
    def gcd_of_strings(str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        length = math.gcd(len(str1), len(str2))
        return str1[:length]

if __name__ == '__main__':
    str_1 = "ABCABC"
    str_2 = "ABC"
    print(Solution().gcd_of_strings(str1=str_1, str2=str_2))
