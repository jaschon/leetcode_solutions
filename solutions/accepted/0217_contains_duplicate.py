#!/usr/bin/env python3
# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/651300596/
# Time: 567ms (58.62%)
# Mem: 26.1 MB (5.86%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums).most_common()
        return c[-1][1] > 1 or c[0][1] > 1

class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for n in nums:
            if n in counter:
                return True
            counter[n] = 1
        return False


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([1,2,3,1], True),
                ([1,2,3,4], False),
                ([1,1,1,3,3,4,3,2,4,2], True),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
