#!/usr/bin/env python3
# 2085. Count Common Words With One Occurrence
# https://leetcode.com/problems/count-common-words-with-one-occurrence/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/621840940/
# Time: 64ms (90.59%)
# Mem: 14.8MB (14.42%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        result = 0
        c1 = Counter(words1)
        c2 = Counter(words2)
        for word in c1:
            if word in c2 and c1[word] == 1 and c2[word] == 1:
                result += 1
        return result

        



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (["leetcode","is","amazing","as","is"], ["amazing","leetcode","is"], 2),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
