#!/usr/bin/env python3
# 228. Summary Ranges
# https://leetcode.com/problems/summary-ranges/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/650649909/
# Time: 38ms (63.96%)
# Mem: 13.9MB (61.40%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        result = []
        tmp = [nums[0],]

        for n in nums:
            if n == tmp[-1]:
                pass
            elif n == tmp[-1]+1:
                tmp.append(n)
            else:
                if len(tmp) == 1:
                    result.append(f'{tmp[0]}')
                else:
                    result.append(f'{tmp[0]}->{tmp[-1]}')
                tmp = [n]
        if tmp:
            if len(tmp) == 1:
                result.append(f'{tmp[0]}')
            else:
                result.append(f'{tmp[0]}->{tmp[-1]}')
        return result





if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                # ([0,1,2,4,5,7], ["0->2","4->5","7"]),
                # ([0,2,3,4,6,8,9], ["0","2->4","6","8->9"]),
                ([-1], ["-1"]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
