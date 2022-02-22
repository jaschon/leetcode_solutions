#!/usr/bin/env python3
# 309. Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/644088465/
# Time: 48ms (70.41%)
# Mem: 18.9MB (23.64%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# dp recurs with memo
# tree:
# branch - buy | skipday
# branch - sell | skipday


class Solution:

    def _loopy(self, prices, index, is_buying):
        if index >= len(prices):
            return 0
        if (index, is_buying) in self.memo:
            return self.memo[(index, is_buying)]

        skipday = self._loopy(prices, index+1, is_buying)

        if is_buying:
            buy = self._loopy(prices, index+1, not is_buying) - prices[index]
            self.memo[(index, is_buying)] = max(buy, skipday)
        else:
            sell = self._loopy(prices, index+2, not is_buying) + prices[index]
            self.memo[(index, is_buying)] = max(sell, skipday)

        return self.memo[(index, is_buying)]
            

    def maxProfit(self, prices: List[int]) -> int:
        self.memo = {}
        return self._loopy(prices, 0, True)
       



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([1,2,3,0,2], 3),



                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
