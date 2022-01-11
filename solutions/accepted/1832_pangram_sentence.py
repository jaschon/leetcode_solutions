#!/usr/bin/env python3
# 1832. Check if the Sentence Is Pangram
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/617742410/
# Time: 44ms (19.36%)
# Mem: 14.2MB (46.02%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return set("abcdefghijklmnopqrstuvwxyz") == set(sentence)
        



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("thequickbrownfoxjumpsoverthelazydog", True),
                ("leetcode", False),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
