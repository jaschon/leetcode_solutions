#!/usr/bin/env python3
# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# EASY

VAL = { "{" : 1000, "[" : 100, "(" : 1, "}": -1000, "]": -100, ")": -1 }

def is_valid(s):
    if all(not x in s for x in ("(]", "[)", "{)", "{]", "[}", "(}")):
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
        ):
        print(example[0], is_valid(example[0]), "=", example[1])

