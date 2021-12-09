#!/usr/bin/env python3



# Easy

# Accepted
# Result: 
# Time:
# Mem:

import sys
sys.path.insert(0,'..')
from _helper import *


### ADD SOLUTION CLASS HERE 


        

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution().
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)

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
