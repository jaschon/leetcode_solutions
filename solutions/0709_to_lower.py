#!/usr/bin/env python3
# 709. To Lower Case
# https://leetcode.com/problems/to-lower-case/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/615063778/
# Time: 46ms (11.58%)
# Mem: 14.3MB (38.42%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""
        for ch in s:
            if ch >= 'A' and ch <= 'Z':
                result += chr(ord(ch)+32)
            else:
                result += ch
        return result


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("Hello", "hello"),
                ("HELLO!", "hello!"),
                ("#$%HE^&%$LLO!", "#$%he^&%$llo!"),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
