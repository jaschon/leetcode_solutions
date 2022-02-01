#!/usr/bin/env python3
# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/632314882/
# Time: 1016ms (83.54%)
# Mem: 25mb (80.69%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        largest, smallest = 0, prices[0]
        for price in prices:
            if price < smallest:
                smallest = price
            largest = max(largest, price-smallest)
        return largest



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([7,1,5,3,6,4], 5), 
                ([7,6,4,3,1], 0),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
