#!/usr/bin/env python3

# https://leetcode.com/problems/rings-and-rods/
# 2103. Rings and Rods

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/605103815/
# Time: 32ms (71.64%)
# Mem: 14.2MB (51.82%)

import sys
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def countPoints(self, rings: str) -> int:
        rods = ["",] * 10 
        cmp = set('RGB')
        for i in range(0, len(rings), 2):
            rods[int(rings[i+1])] += rings[i]
        return len([_ for _ in rods if cmp == set(_)])

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution().countPoints  ,
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("B0B6G0R6R0R6G9", 1),
                ("B0R0G0R9R0B0G0", 1),
                ("G4", 0),
                ):

            funct = f
            print()

            ### ADD EXTRA PARAM AFTER e[0]...
            test(funct, e[-1], e[0])

            ### NODE VERSION OF TEST
            # test_node(funct, cmp, val)

            # timer(funct, e[0])
            # timer_amt(funct, 10, e[0])

            print()
