#!/usr/bin/env python3

# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/

# Easy

# Accepted (Solution2)
# Result: https://leetcode.com/submissions/detail/613044043/
# Time: 60ms (5.37%)
# Mem: 14.2 MB (67.43)

# Accepted (Solution 1A)
# Result: https://leetcode.com/submissions/detail/613045564/
# Time: 28ms (85.85%)
# Mem: 14.4 (38.25%)

# Accepted (Solution 1B)
# Result: https://leetcode.com/submissions/detail/613048072/
# Time: 20ms (99.19%)
# Mem 14.4 MB (38.25%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution2:
    def hammingWeight(self, n: int) -> int:
        return f'{n:b}'.count('1')

# B (Faster????)
class Solution:
    def hammingWeight(self, n: int) -> int:
        return len([1 for _ in f'{n:b}' if _ == '1'])

# A
class Solution3:
    def hammingWeight(self, n: int) -> int:
        return len([_ for _ in f'{n:b}' if _ == '1'])


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (11,3),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
