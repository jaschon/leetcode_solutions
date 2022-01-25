#!/usr/bin/env python3
# 1773. Count Items Matching a Rule
# https://leetcode.com/problems/count-items-matching-a-rule/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/627652750/
# Time: 240ms (85.45%)
# Mem: 20.7MB (22.73%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
rule = { 'type': 0, 'color': 1, 'name': 2}
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return len([i for i in items if i[rule[ruleKey]] == ruleValue])



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver", 1),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
