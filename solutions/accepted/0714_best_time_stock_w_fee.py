#!/usr/bin/env python3
# 714. Best Time to Buy and Sell Stock with Transaction Fee
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/646819562/
# Time: 1174ms (42.12%)
# Mem: 21MB (94.56%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# loop, keep track of total if you sell (max keep price + price - fee)
# and total of if you keep

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        result = 0
        keep = -prices[0]
        for price in prices:
            result = max(result, keep + price - fee)
            keep = max(keep, result - price)
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
                ([1,3,2,8,4,9], 2, 8),
                ([1,3,7,5,10,3], 3, 6),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
