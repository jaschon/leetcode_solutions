#!/usr/bin/env python3
# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# EASY

# APL VERSION
# s ← 'A man, a plan, a canal: Panama'
# clean ← {819⌶ ⍵~' ,:!'}
# pal ←{⊣ ≡ ⌽ clean ⍵}
# pal s

import re

def is_palindrome(s=[]):
    s = re.sub(r'[^A-Za-z0-9]+', "", s).lower()
    return s == s[::-1]

if __name__ == "__main__":
    funct = is_palindrome
    for example in (
            (" ", True),
            ("tacocat!", True),
            ("race a car", False),
            ("A man, a plan, a canal: Panama", True),
        ):

        print(example[0], funct(example[0]), "=", example[1])
