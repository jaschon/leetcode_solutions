#!/usr/bin/env python3
# 740. Delete and Earn
# https://leetcode.com/problems/delete-and-earn/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/638727432/ 
# Time: 52ms
# Mem: 14.2MB

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        mapper = Counter(nums)
        prev = 0
        total = 0
        for value in range(max(mapper.keys())+1): #loop through keys
            prev, total = total, max(prev + value * mapper[value], total) #get the larger of value total count 
        return total



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([2,2,3,3,3,4], 9),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
