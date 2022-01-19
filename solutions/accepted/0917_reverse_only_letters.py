#!/usr/bin/env python3
# 917. Reverse Only Letters
# https://leetcode.com/problems/reverse-only-letters/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/623346959/
# Time: 24ms (96.40%)
# Mem: 14.4MB

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
import re
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alpha = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        clean = list(re.sub("[^a-zA-Z]", "", s))
        s = list(s)
        for i in range(len(s)):
            if s[i] in alpha:
                s[i] = clean.pop()
        return "".join(s)

class Solution2:
    def reverseOnlyLetters(self, s: str) -> str:
        clean = [_ for _ in s if _.isalpha()]
        s = list(s)
        for i in range(len(s)):
            if s[i].isalpha():
                s[i] = clean.pop()
        return "".join(s)

class Solution3:
    def reverseOnlyLetters(self, s: str) -> str:
        clean = [_ for _ in s if _.isalpha()]
        s = list(s)
        for i in range(len(s)):
            s[i] = clean.pop() if s[i].isalpha() else s[i]
        return "".join(s)


class Solution4:
    def reverseOnlyLetters(self, s: str) -> str:
        clean = [_ for _ in s if _.isalpha()]
        s = list(s)
        result = ""
        for i in range(len(s)):
            result += clean.pop() if s[i].isalpha() else s[i]
        return result

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            Solution3(),
            Solution4(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("ab-cd", "dc-ba"),
                ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
                ("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntse-T!"),



                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
