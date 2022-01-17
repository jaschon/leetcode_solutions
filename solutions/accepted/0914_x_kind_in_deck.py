#!/usr/bin/env python3
# 914. X of a Kind in a Deck of Cards
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/621955012/
# Time: 127ms (94.13%)
# Mem: 14.5MB (64.04%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from math import gcd
from functools import reduce
from collections import Counter
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return reduce(gcd, Counter(deck).values()) > 1

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([1,2,3,4,4,3,2,1], True),
                ([1,1,1,2,2,2,3,3], False),
                ([1], False),
                ([1,1,2,2,2,2], True),
                ([1,1,1,1,2,2,2,2,2,2], True),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
