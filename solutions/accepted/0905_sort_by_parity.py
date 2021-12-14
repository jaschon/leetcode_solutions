#!/usr/bin/env python3


# 905. Sort Array By Parity
# https://leetcode.com/problems/sort-array-by-parity/
# Easy

# Accepted #1
# Result: https://leetcode.com/submissions/detail/601783424/
# Time: 187ms
# Mem: 15.2MB

# Accepted #2
# Result: https://leetcode.com/submissions/detail/601784164/
# Time: 88ms (27.87%)
# Mem: 15.2MB (25.32%)

# Accepted Final !!!!
# Result: https://leetcode.com/submissions/detail/601786604/
# Time: 72ms (94.82%)
# Mem: 15MB (58.09%)

import sys
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

#FINAL
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums,key=lambda x: x%2)

class Solution1:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [_ for _ in nums if _%2 == 0] + [_ for _ in nums if _%2 != 0]

class Solution2:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            if n%2 == 0:
                result.insert(0, n)
            else:
                result.append(n)
        return result


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution().sortArrayByParity,
            Solution1().sortArrayByParity,
            Solution2().sortArrayByParity,
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([3,1,2,4], [2,4,3,1]),
                ([0], [0]),
                ([0,1], [0,1]),

                ):

            funct = f
            print()

            ### ADD EXTRA PARAM AFTER e[0]...
            test(funct, e[-1], e[0])

            ### NODE VERSION OF TEST
            # test_node(funct, cmp, val)

            timer(funct, e[0])
            # timer_amt(funct, 10, e[0])

            print()
