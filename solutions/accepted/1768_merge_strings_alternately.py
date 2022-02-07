#!/usr/bin/env python3
# 1768. Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/

# Easy

# Accepted
# Result: https://leetcode.com/problems/merge-strings-alternately/submissions/
# Time: 36ms (58.15%)
# Mem: 19.9 MB (93.80%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from itertools import zip_longest, chain

class Solution3:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(e for t in zip_longest(word1, word2, fillvalue="") for e in t)

class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(chain(*zip_longest(word1, word2, fillvalue="")))


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(z for z in chain(*zip_longest(word1, word2, fillvalue="")))


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("abc", "pqr", "apbqcr"),
                ("ab", "pqrs", "apbqrs"),
                ("abcd", "pq", "apbqcd"),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
