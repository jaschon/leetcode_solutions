#!/usr/bin/env python3
# 72. Edit Distance
# https://leetcode.com/problems/edit-distance/

# Hard

# Accepted
# Result: https://leetcode.com/submissions/detail/660579667/
# Time: 120ms (93.70%)
# Mem: 19.9MB (13.78%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:

    def __init__(self):
        self.memo = {}

    def minDistance(self, word1: str, word2: str) -> int:

        if (word1,word2) in self.memo:
            return self.memo[(word1,word2)]

        if not word1 or not word2:
            return len(word1) + len(word2) #<-need to return num of chars left that haven't been changed.

        if word1[0] != word2[0]: #check if first chars don't match
            self.memo[(word1, word2)] = min(
                    1+self.minDistance(word1[1:], word2), #remove word1's first

                    1+self.minDistance(word1, word2[1:]), #remove word2's first

                    1+self.minDistance(word1[1:], word2[1:]), #replace both

                    )
            return self.memo[(word1,word2)]

        self.memo[(word1,word2)] = self.minDistance(word1[1:], word2[1:])
        return self.memo[(word1,word2)]


        



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("horse", "ros", 3),
                ("intention", "execution", 5),



                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
