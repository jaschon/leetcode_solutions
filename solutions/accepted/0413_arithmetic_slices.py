#!/usr/bin/env python3
# 413. Arithmetic Slices
# https://leetcode.com/problems/arithmetic-slices/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/652648297/
# Time: 40ms (85.03%)
# Mem: 14.2MB (75.02%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# 1. loop through nums (start at 2, so we can check i-1 and i-2)
# 2. if (nums[i]-nums[i-1) is the same as (nums[i-1]-nums[i-2])
#         inc counter
#    else update result
#    which is result + (count*count+1)//2


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        count = result = 0

        for i in range(2, len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                count += 1
            else:
                result = result + (count*(count+1))//2
                count = 0

        return result + (count * (count+1))//2        



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([1,2,3,4], 3),
                ([1], 0),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
