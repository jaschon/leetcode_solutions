#!/usr/bin/env python3
# 860. Lemonade Change
# https://leetcode.com/problems/lemonade-change/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/614308364/
# Time: 828ms (75.00%)
# Mem: 18.3MB (63.04%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = {5:0, 10:0, 20:0}
        for b in bills:
            money[b] += 1
            if b == 10: 
                if money[5] > 0:
                    money[5] -= 1
                else:
                    return False
            elif b == 20:
                if money[10] > 0 and money[5] > 0:
                    money[5] -= 1
                    money[10] -=1
                elif money[5] > 2:
                    money[5] -= 3
                else:
                    return False
        return True




if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([5,5,5,10,20], True),
                ([5,5,10,10,20], False),
                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
