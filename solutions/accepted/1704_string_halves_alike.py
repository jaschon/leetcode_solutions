#!/usr/bin/env python3
# 1704. Determine if String Halves Are Alike
# https://leetcode.com/problems/determine-if-string-halves-are-alike/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/619122299/
# Time: 36ms (68.54%)
# Mem: 14.5MB (7.23%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ('a','e','i','o','u','A','E','I','O','U')
        length = len(s)//2
        len1 = len([c for c in s[:length] if c in vowels])
        len2 = len([c for c in s[length:] if c in vowels])
        return len1 == len2
        
class Solution2:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        vowels = ('a','e','i','o','u')
        length = len(s)//2
        len1 = len([c for c in s[:length] if c in vowels])
        len2 = len([c for c in s[length:] if c in vowels])
        return len1 == len2


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("book", True),
                ("textbook", False),

                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
