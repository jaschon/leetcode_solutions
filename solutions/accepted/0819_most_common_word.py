#!/usr/bin/env python3

# 819. Most Common Word
# https://leetcode.com/problems/most-common-word/
# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/621822709/
# Time: 25ms (96.58%)
# Mem: 14.5 (19.74%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub("[!?\',;.]", " ", paragraph).lower()
        for word in Counter(paragraph.split()).most_common():
            if word[0] not in banned:
                return word[0]
        return ""

        



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"], "ball"),
                ("a, a, a, a, b,b,b,c, c", ["a"], "b"),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
