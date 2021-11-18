#!/usr/bin/env python3
# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# EASY
# Accepted!
# https://leetcode.com/submissions/detail/589234777/
# 24ms (96.31%)
# 14.2MB (87.15%)

VAL = { "{" : 1000, "}": -1000, "[" : 100, "]": -100, "(" : 1, ")": -1 }
FAIL =  ("(]", "[)", "{)", "{]", "[}", "(}", "[([]])",)

class Solution:
    def isValid(self, s):
        if s[-1] in "[{(" or s[0] in "]})": return False
        if all(not x in s for x in FAIL):
            return sum(VAL.get(ch) for ch in s) == 0
        return False

if __name__ == "__main__":

    for example in (
            ("()", True),
            ("()[]{}", True),
            ("(]", False),
            ("(}", False),
            ("{)", False),
            ("([)]", False),
            ("{[]}", True),
            ("{[()]", False),
            ("{{[()]}}(){}[][({})]({[]})", True),

            ("[({(())}[()])]", True), # failed!
            ("[][", False),
            ("(){}}{", False),
            ("[([]])", False),
        ):
        print(example[0], "PASS" if Solution().isValid(example[0]) == example[1] else "FAIL")

