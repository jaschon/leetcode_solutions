#!/usr/bin/env python3

# 1108. Defanging an IP Address
# https://leetcode.com/problems/defanging-an-ip-address/


# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/612266461/
# Time: 49ms (6.80%) (Slow site???? Solution is the SAME code as the fastest. ???)
# Mem: 14.1 MB (65.80%)

import sys
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution().defangIPaddr  ,
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("1.1.1.1", "1[.]1[.]1[.]1"),
                ("255.100.50.0", "255[.]100[.]50[.]0"),


                ):

            funct = f
            print()

            ### ADD EXTRA PARAM AFTER e[0]...
            test(funct, e[-1], e[0])

            ### NODE VERSION OF TEST
            # test_node(funct, cmp, val)

            # timer(funct, e[0])
            # timer_amt(funct, 10, e[0])

            print()
