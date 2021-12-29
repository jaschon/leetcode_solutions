#!/usr/bin/env python3
# 2114. Maximum Number of Words Found in Sentences
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

# Easy

# Accepted (Solution)
# Result: https://leetcode.com/submissions/detail/609349591/
# Time: 36ms (93.42%)
# Mem: 14.3 MB (42.36%)

import sys
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        most = 0
        for s in sentences:
            length = len(s.split())
            most = length if length > most else most
        return most

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution1().mostWordsFound  ,
            Solution().mostWordsFound  ,
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (["alice and bob love leetcode", "i think so too", "this is great thanks very much"], 6),


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
