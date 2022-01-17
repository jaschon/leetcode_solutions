#!/usr/bin/env python3
# 884. Uncommon Words from Two Sentences
# https://leetcode.com/problems/uncommon-words-from-two-sentences/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/621836231/
# Time: 28ms (88.55%)
# Mem: 14.3MB (25%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        result = []
        c1 = Counter(s1.split())
        c2 = Counter(s2.split())
        for arr, cmp in ((c1,c2), (c2,c1)):
            for word in arr:
                if arr[word] == 1 and word not in cmp:
                    result.append(word)
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
                ("this apple is sweet", "this apple is sour", ["sweet","sour"]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
