#!/usr/bin/env python3
# 376. Wiggle Subsequence
# https://leetcode.com/problems/wiggle-subsequence/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/659913220/
# Time: 56ms (47.94%)
# Mem: 13.8MB (87.51%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        length = len(nums)
        
        if length < 2:
            return length
        
        up = down = 1
        
        for i in range(1,length):
            if nums[i] < nums[i-1]:
                down = 1 + up
            elif nums[i] > nums[i-1]:
                up = 1 + down
                
        return max(up, down)


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([1,7,4,9,2,5], 6),
                ([1,17,5,10,13,15,10,5,16,8], 7),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
