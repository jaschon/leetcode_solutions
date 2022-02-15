#!/usr/bin/env python3
# 918. Maximum Sum Circular Subarray
# https://leetcode.com/problems/maximum-sum-circular-subarray/

# Medium

# Accepted
# Result: https://leetcode.com/problems/maximum-sum-circular-subarray/submissions/
# Time: 569ms (71.33%)
# Mem: 19MB (32.48%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        total_sum = sum(nums)

        max_current = min_current = max_count = min_count = nums[0]

        for n in nums[1:]:
            max_current = max(max_current + n, n)
            min_current = min(min_current + n, n)

            max_count = max(max_count, max_current)
            min_count = min(min_count, min_current)

        return max_count if min_count == total_sum else max(max_count, total_sum - min_count)



class Solution1:
    def maxSubarraySumCircular(self, a: List[int]) -> int:
        n = len(a)
     
        # Corner Case
        if (n == 1):
            return a[0]
     
        # Initialize sum variable which
        # store total sum of the array.
        sum = 0
        for i in range(n):
            sum += a[i]
     
        # Initialize every variable
        # with first value of array.
        curr_max = a[0]
        max_so_far = a[0]
        curr_min = a[0]
        min_so_far = a[0]
     
        # Concept of Kadane's Algorithm
        for i in range(1, n):
           
            # Kadane's Algorithm to find Maximum subarray sum.
            curr_max = max(curr_max + a[i], a[i])
            max_so_far = max(max_so_far, curr_max)
     
            # Kadane's Algorithm to find Minimum subarray sum.
            curr_min = min(curr_min + a[i], a[i])
            min_so_far = min(min_so_far, curr_min)
        if (min_so_far == sum):
            return max_so_far
     
        # returning the maximum value
        return max(max_so_far, sum - min_so_far)






if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution1(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([1,-2,3,-2], 3),
                ([-4,-7,-9,-8,6,7,-10,-6,9,2], 13),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
