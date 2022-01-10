#!/usr/bin/env python3
# https://leetcode.com/problems/reverse-words-in-a-string-iii/
# 557. Reverse Words in a String III

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/617232501/
# Time: 59ms (40.41%)
# Mem: 14.8MB (62.71%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(_[::-1] for _ in s.split())



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
