#!/usr/bin/env python3
# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/647520862/
# Time: 54ms (25.96%)
# Mem: 14.1MB (55.50%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
mapper = {}
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if (m,n) in mapper:
            return mapper[(m,n)]
        if m == 1 and n == 1:
            return 1
        if 0 in (m,n):
            return 0
        mapper[(m,n)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return mapper[(m,n)]



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (3,7,28),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
