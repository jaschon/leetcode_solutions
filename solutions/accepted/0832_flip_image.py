#!/usr/bin/env python3
# 832. Flipping an Image
# https://leetcode.com/problems/flipping-an-image/

# Easy

# Accepted
# Result: 
# Time:
# Mem:

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# class Solution2:
#     def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
#         for row in range(len(image)):
#             image[row] = [1-i for i in reversed(image[row])]
#         return image

        
# class Solution:
#     def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
#         return [[1-i for i in row[::-1]] for row in image]

class Solution3:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[1-i for i in reversed(row)] for row in image]

class Solution4:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[i^1 for i in reversed(row)] for row in image]

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            # Solution(),
            # Solution2(),
            Solution4(),
            Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([[1,1,0],[1,0,1],[0,0,0]], [[1,0,0],[0,1,0],[1,1,1]]),
                ([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]], [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 100, *e[:-1])


            print()
