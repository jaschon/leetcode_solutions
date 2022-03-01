#!/usr/bin/env python3
# 377. Combination Sum IV
# https://leetcode.com/problems/combination-sum-iv/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/650855515/
# Time: 52ms (62.06%)
# Mem: 14.2MB (51.59%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        def loop(target):
            if target == 0:
                return 1
            if target < 0:
                return 0
            if target in self.memo:
                return self.memo[target]

            total = 0
            for n in nums:
                total += loop(target-n)
                self.memo[target] = total
            return total

        self.memo = {}
        return loop(target)


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([1,2,3], 4, 7),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
