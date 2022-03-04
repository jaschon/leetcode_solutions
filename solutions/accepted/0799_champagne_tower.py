#!/usr/bin/env python3
# 799. Champagne Tower
# https://leetcode.com/problems/champagne-tower/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/653328603/
# Time: 240ms (27.67%)
# Mem: 14MB (81.55%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        current_row = [poured]
        for i in range(query_row):
            next_row = [0 for _ in range(len(current_row)+1)] 
            for j in range(len(current_row)):
                overflow = max(0, current_row[j]-1)
                next_row[j] = next_row[j] + overflow/2 or overflow/2
                next_row[j+1] = next_row[j+1] + overflow/2 or overflow/2

            current_row = next_row

        return min(1, current_row[query_glass])



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (1,1,1, 0.00000),
                (2,1,1, .500000),
                (100000009, 33, 17, 1.00000),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
