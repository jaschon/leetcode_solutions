#!/usr/bin/env python3
# https://leetcode.com/problems/palindrome-number/
# 9. Palindrome Number
# Easy
# Accepted
# https://leetcode.com/submissions/detail/589301283/
# 48ms (95.99%)
# 14.3 MB (16.89%)

class Solution(object):
    def isPalindrome(self, x):
        if x < 0: return False
        x = str(x)
        return x == x[::-1]

if __name__ == "__main__":
    funct = Solution().isPalindrome
    for ex in (
            (121, True),
            (-121, False),
            (10, False),
            (-101, False),
            ):
        result = funct(ex[0])
        print(ex[0], result, "PASS" if result == ex[1] else "FAIL")





