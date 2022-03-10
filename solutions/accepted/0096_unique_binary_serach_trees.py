#!/usr/bin/env python3
# 96. Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/656062212/
# Time: 32ms (84.87%)
# Mem: 13.9MB (78.11%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# dp!
# 1. make a cache array. set defaults to '1'. length is n +1
# 2. loop through range starting at 2 (node 1 and node 0 are always 1)
# 3. clear total
# 4. loop through 1-(nodes+1)
# 5. all left sides is root-1  left --> [1] -2- [3,4,5] <--right
# 6. all right side is node-root
# 7. cal total (number left * number right)
# 8. store in cache
# 9. return cache[n]


class Solution:
    def numTrees(self, n: int) -> int:
        trees = [1] * (n +1)
        for nodes in range(2, n+1):
            total = 0
            for root in range(1, nodes+1):
                left = root-1
                right = nodes-root
                total += trees[left] * trees[right]
            trees[nodes] = total
        return trees[n]
        



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (3,5),
                (1,1),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
