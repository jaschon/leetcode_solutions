#!/usr/bin/env python3
# 198. House Robber
# https://leetcode.com/problems/house-robber/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/638688506/
# Time: 50ms (32.40%)
# Mem: 13.8MB (93.64%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def rob(self, nums: List[int]) -> int:
        even = 0
        odd = 0
        flip = False
        for n in nums:
            if flip:
                even = max(even + n, odd)
            else:
                odd = max(odd + n, even)
            flip = not flip
        return max(even, odd)


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([1,2,3,1], 4),
                ([2,7,9,3,1], 12),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
