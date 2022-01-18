#!/usr/bin/env python3

# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/622611640/
# Time: 43ms (42.52%)
# Mem: 14.6MB (13.36%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s[::-1].split() if word])


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("the sky is blue", "blue is sky the"),
                ("  hello world  ", "world hello"),
                ("      abc def        ghij", "ghij def abc"),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
