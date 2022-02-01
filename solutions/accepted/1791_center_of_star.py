#!/usr/bin/env python3
# 1791. Find Center of Star Graph
# https://leetcode.com/problems/find-center-of-star-graph/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/632405523/
# Time: 2113ms (5.08%)
# Mem: 49.5MB (99.00%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from collections import Counter
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        c = Counter()
        for e in edges:
            c.update(e)
        return c.most_common(1)[0][0]




if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([[1,2],[2,3],[4,2]], 2),
                ([[1,2],[5,1],[1,3],[1,4]], 1)


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
