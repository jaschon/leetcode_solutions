#!/usr/bin/env python3
# 1720. Decode XORed Array
# https://leetcode.com/problems/decode-xored-array


# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/618522931/
# Time: 220ms (91.61%)
# Mem: 16MB

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first,]
        for n in encoded:
            result.append(result[-1]^n)
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
                ([1,2,3], 1, [1,0,2,1]),
                ([6,2,7,3], 4, [4,2,0,7,4]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
