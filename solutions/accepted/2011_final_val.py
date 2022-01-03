#!/usr/bin/env python3
# 2011. Final Value of Variable After Performing Operations
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/612257995/ 
# Time: 86ms (~7.73%) (Site slow???) 
# Mem: 14.3mb
 
import sys
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for i in operations:
            result += 1 if i[1] == "+" else -1
        return result

ops = {"+" : 1, "-": -1}
class Solution1:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum([ops[_[1]] for _ in operations])

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution().finalValueAfterOperations  ,
            Solution1().finalValueAfterOperations  ,
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)

                (["--X","X++","X++"], 1),
                (["++X","++X","X++"], 3),
                (["X++","++X","--X","X--"], 0),

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
