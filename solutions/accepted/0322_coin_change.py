#!/usr/bin/env python3 # 322. Coin Change
# https://leetcode.com/problems/coin-change/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/650738061/
# Time: 2896 ms (14.29%)
# Mem: 13.9MB (97.98%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [inf] * (amount+1)
        table[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a >= c:
                    table[a] = min(table[a], table[a-c]+1)

        return table[amount] if table[amount] != inf else -1


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([1,2,5], 11, 3),
                ([2], 3, -1),
                ([3,7,405,436], 8839, 37),
                ([1], 0, 0),
                ([186,419,83,408], 6249, 20),


                ):

            # funct = inspect.getmembers(f)[-1][1]
            funct = f.coinChange

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
