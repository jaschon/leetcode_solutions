#!/usr/bin/env python3
# 1014. Best Sightseeing Pair
# https://leetcode.com/problems/best-sightseeing-pair/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/643341027/
# Time: 895ms (13.05%)
# Mem: 20.6 MB (13.51%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_val = values[0]
        result = 0
        for i in range(1, len(values)):
            max_val = max(max_val, values[i-1] + i - 1)
            result = max(result, max_val + values[i] - i)
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
                ([8,1,5,2,6], 11),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
