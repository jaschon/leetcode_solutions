#!/usr/bin/env python3
# 1470. Shuffle the Array
# https://leetcode.com/problems/shuffle-the-array/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/612289630/
# Time: 56ms (88.73)
# Mem: 14.6MB (17.35%)

import sys
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
import itertools
class Solution1:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return list(itertools.chain(*zip(nums[:n], nums[n:])))

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for x, y in zip(nums[:n], nums[n:]):
            result.append(x)
            result.append(y)
        return result
        
if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution().shuffle  ,
            Solution1().shuffle  ,
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
               ([2,5,1,3,4,7], 3, [2,3,5,4,1,7]),


                ):

            funct = f
            print()

            ### ADD EXTRA PARAM AFTER e[0]...
            test(funct, e[-1], e[0], e[1])

            ### NODE VERSION OF TEST
            # test_node(funct, cmp, val)

            timer(funct, e[0], e[1])
            # timer_amt(funct, 10, e[0])

            print()
