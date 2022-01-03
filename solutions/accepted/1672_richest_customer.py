#!/usr/bin/env python3
# 1672. Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/612271692/
# Time: 52ms (77.57%)
# Mem: 14.4 MB (29.40%)

import sys
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution1:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(_) for _ in accounts)


### ADD SOLUTION CLASS HERE 
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(lambda x: sum(x), accounts))

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution().maximumWealth ,
            Solution1().maximumWealth ,
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([[1,2,3],[3,2,1]], 6),


                ):

            funct = f
            print()

            ### ADD EXTRA PARAM AFTER e[0]...
            test(funct, e[-1], e[0])

            ### NODE VERSION OF TEST
            # test_node(funct, cmp, val)

            timer(funct, e[0])
            # timer_amt(funct, 10, e[0])

            print()
