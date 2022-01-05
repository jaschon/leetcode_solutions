#!/usr/bin/env python3
# 1221. Split a String in Balanced Strings
# https://leetcode.com/problems/split-a-string-in-balanced-strings/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/613714001/
# Time: 28ms (84.76%)
# Mem: 14.2MB (68.84%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        count = {'L':0,'R':0}
        for ch in s:
            count[ch] += 1
            if count['L'] == count['R']:
                result += 1
                count['L'], count['R'] = 0,0
        return result


# Faster??
class Solution2:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        count = {'L':0,'R':0}
        for ch in s:
            count[ch] += 1
            result = result + 1 if count['L'] == count['R'] else result
        return result

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("RLRRLLRLRL", 4),
                ("RLLLLRRRLR", 3),
                ("LLLLRRRR", 1),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
