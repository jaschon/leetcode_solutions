#!/usr/bin/env python3
# 55. Jump Game
# https://leetcode.com/problems/jump-game/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/653330021/
# Time: 685ms (43.08%)
# Mem: 15.3 MB (52.68%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        length = len(nums)

        if length <= 1:
            return True

        last = length - 1

        for i in range(last, -1, -1):

            if i + nums[i] >= last:
                last = i

        return last == 0


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([2,3,1,1,4], True),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
