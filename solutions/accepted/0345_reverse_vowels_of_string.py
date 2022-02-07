#!/usr/bin/env python3
# 345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/636617440/ 
# Time: 77ms (48.18%)
# Mem: 16.6MB (11.50%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution2:
    def reverseVowels(self, s: str) -> str:
        result = []
        vset = set("aeiouAEIOU")
        vowels = [l for l in s[::-1] if l in vset]
        for l in s:
            result.append(vowels.pop(0) if l in vset else l)
        result.extend(vowels)
        return "".join(result)

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [i for i,l in enumerate(s) if l in set("aeiouAEIOU")]
        result = list(s)
        for i, v in enumerate(vowels):
            result[v] = s[vowels[-1-i]]
        return "".join(result)

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("leetcode", "leotcede"),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
