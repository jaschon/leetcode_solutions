#!/usr/bin/env python3
# 2000. Reverse Prefix of Word
# https://leetcode.com/problems/reverse-prefix-of-word/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/615055297/
# Time: 32ms (60.88%)
# Mem: 14.4MB (10.33%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if not ch in word: return word
        return word[:word.index(ch)+1][::-1] + word[word.index(ch)+1:]
        



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("abcdefd", "d", "dcbaefd"),
                ("xyxzxe", "z", "zxyxxe"),
                ("abcd", "z", "abcd"),



                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
