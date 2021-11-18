#!/usr/bin/env python3
# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# EASY
# Accepted!
# https://leetcode.com/submissions/detail/589197648/
# 40ms (90.49%)
# 15.4 (30.29%)

# APL VERSION
# s ← 'A man, a plan, a canal: Panama'
# clean ← {819⌶ ⍵~' ,:!'}
# pal ←{⊣ ≡ ⌽ clean ⍵}
# pal s

import re

class Solution:
    def isPalindrome(self, s=[]):
        s = re.sub(r'[^A-Za-z0-9]+', "", s).lower()
        return s == s[::-1]

if __name__ == "__main__":
    for example in (
            (" ", True),
            ("tacocat!", True),
            ("race a car", False),
            ("A man, a plan, a canal: Panama", True),
        ):
        s = Solution()
        print(example[0], s.isPalindrome(example[0]), "=", example[1])
