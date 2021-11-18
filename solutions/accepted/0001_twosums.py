#!/usr/bin/env python3
#1. Two Sum
#https://leetcode.com/problems/two-sum/
# Easy
# Accepted!
# https://leetcode.com/submissions/detail/589155977/
# Runtime: 512ms.
# MEM 14.4MB


import timeit, functools

# SUBMITTED CLASS
class Solution(object):

    def twoSum(self, nums, target):
        """Two Sums Sub"""
        for i1, n1 in enumerate(nums):
            sub = target-n1
            if sub in nums:
                match = nums.index(sub)
                if match > -1 and i1 != match:
                    return [i1, match]
        return []

    def twoSums_br(self, nums, target):
        """Two Sums Brute Force"""
        for i1 in range(len(nums)):
            for i2 in range(len(nums)):
                if i1 != i2 and (nums[i1]+nums[i2]) == target:
                    return [i1,i2]
        return []

if __name__ == "__main__":
    for ex in (
            ([2,7,11,15], 9, [0,1]),
            ([3,2,4], 6, [1,2]),
            ([3,3], 6, [0,1]),
            ([3,2,3], 6, [0,2]),
            ):
        s = Solution()
        t = timeit.Timer(functools.partial(s.twoSum, ex[0], ex[1])) 
        print(ex[0], "--" , s.twoSum(ex[0], ex[1]), "--", t.timeit(5))





