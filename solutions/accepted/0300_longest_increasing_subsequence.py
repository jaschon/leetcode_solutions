#!/usr/bin/env python3
# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/657405778/
# Time: 4608ms (42.92%)
# Mem: 14.1MB (90.96%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# 1. dp!
# 2. make a table
# 3. loop backwards
# 4. loop forwards, starting i+1
# 5. if number in i index is less than number in j index
# a) set the index of i in table to the max of table[i] or table[j]+1
# 6. return max number in table

class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:

        result = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    result[i] = max(result[i], result[j]+1)

        return max(result)


        


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([10,9,2,5,3,7,101,18], 4),
                ([0,1,0,3,2,3], 4),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
