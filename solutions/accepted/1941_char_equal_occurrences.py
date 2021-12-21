#!/usr/bin/env python3
# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
# 1941. Check if All Characters Have Equal Number of Occurrences

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/605130289/
# Time: 32ms (81.22%)
# Mem: 14.3MB (63.88%)

import sys
sys.path.insert(0,'..')
from _helper import *
from typing import List


from collections import Counter
### ADD SOLUTION CLASS HERE 
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        common = count.most_common()
        return common[0][1] == common[-1][1]


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution().areOccurrencesEqual  ,
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("abacbc", True),
                ("aaabb", False),


                ):

            funct = f
            print()

            ### ADD EXTRA PARAM AFTER e[0]...
            test(funct, e[-1], e[0])

            ### NODE VERSION OF TEST
            # test_node(funct, cmp, val)

            # timer(funct, e[0])
            # timer_amt(funct, 10, e[0])

            print()
