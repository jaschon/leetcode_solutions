#!/usr/bin/env python3
# 1079. Letter Tile Possibilities
# https://leetcode.com/problems/letter-tile-possibilities/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/618404387/
# Time: 72ms (75.90%)
# Mem: 15.3MB (63.91%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

from itertools import permutations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = set()
        for i in range(1, len(tiles)+1):
            for el in permutations(tiles, i):
                result.add("".join(el))
        return len(result)





if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("AAB", 8),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
