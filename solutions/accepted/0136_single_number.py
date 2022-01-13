#!/usr/bin/env python3
# 136. Single Number
# https://leetcode.com/problems/single-number/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/619229201/
# Time: 136ms (61.79%)
# Mem: 16.9MB (19.77%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[-1][0]



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([4,1,2,1,2], 4),
                ([2,2,1], 1),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
