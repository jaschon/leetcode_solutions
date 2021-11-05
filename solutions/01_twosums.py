#!/usr/bin/env python3
#1. Two Sum
#https://leetcode.com/problems/two-sum/
# Easy

import timeit, functools

def twosums_br(nums, target):
    """Two Sums Brute Force"""
    for i1 in range(len(nums)):
        for i2 in range(len(nums)):
            if i1 != i2 and (nums[i1]+nums[i2]) == target:
                return [i1,i2]
    return []

def twosums_sub(nums, target):
    """Two Sums Sub"""
    for i1, n1 in enumerate(nums):
        match = nums.index(target-n1)
        if match > -1 and i1 != match:
            return [i1, match]
    return []


if __name__ == "__main__":
    functs = (twosums_sub, twosums_br)
    for funct in functs:
        for ex in (
                ([2,7,11,15], 9, [0,1]),
                ([3,2,4], 6, [1,2]),
                ([3,3], 6, [0,1]),

                ):
            t = timeit.Timer(functools.partial(funct, ex[0], ex[1])) 
            print(funct.__doc__, "--", ex[0], "--" , funct(ex[0], ex[1]), "--", t.timeit(5))





