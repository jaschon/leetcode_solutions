#!/usr/bin/env python3
# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/637984097/
# Time: 65ms (59.57%)
# Mem: 14mb (96.47%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# can start on 2nd step
# use the cost array to make a running sum of the min value in the next 2
# return the min value in the last 2


class Solution1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([10,15,20], 15),
                ([1,100,1,1,1,100,1,1,100,1], 6),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
