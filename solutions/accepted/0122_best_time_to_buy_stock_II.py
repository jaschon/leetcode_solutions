#!/usr/bin/env python3
# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/643352681/
# Time: 88ms (46.41%)
# Mem: 15.2MB (41.95%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# if price is greater than the prev price
# add price[i] - price[i-1] to your total
# return total

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                result += (prices[i] - prices[i-1])
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
                ([7,1,5,3,6,4], 7),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
