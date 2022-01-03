#!/usr/bin/env python3
# 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/612386332/
# Time: 32ms (63.84%)
# Mem: 14.3MB)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len([_ for _ in stones if _ in jewels])

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("aA", "aAAbbbb", 3),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
