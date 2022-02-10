#!/usr/bin/env python3
# 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/638667534/
# Time: 379ms (38.19%)
# Mem: 16.5 MB (99.49%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

#make running total. check if total sum (total) - target (k) is in dict, if so add 1 to counter
# add/update mapper count  (mapper[total] + 1)


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapper = {0: 1} #start with 0 in array to check for single item arrays
        total = 0
        count = 0
        for n in nums:
            total += n
            if total-k in mapper:
                count += mapper[total-k]
            mapper[total] = mapper.get(total,0) + 1
        return count



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([1,1,1], 2, 2),
                ([1,2,3], 3, 2),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
