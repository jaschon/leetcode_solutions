#!/usr/bin/env python3
# 1081. Smallest Subsequence of Distinct Characters
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/662485450/ 
# Time: 63ms (15.43%)
# Mem: 14MB (35.99%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List

#SAME AS #316!

### ADD SOLUTION CLASS HERE 
# greedy!
# 1. map the last index of each char to a dict
# 2. loop through chars
# 3a. if seen before, skip
# 3b. else while loop, pop out (and remove from seen) if the char is lower alpha and it has a higher index than found in the map
# 4. add to stack and seen
# 5. return stack joined

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        mapper = { char: index for index, char in enumerate(s) }
        stack, seen = [], set()
        for index, char in enumerate(s):
            if not char in seen:
                while stack and char < stack[-1] and mapper[stack[-1]] > index:
                    seen.remove(stack[-1])
                    stack.pop()
                stack.append(char)
                seen.add(char)
        return "".join(stack)


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("bcabc", "abc"),
                ("cbacdcbc", "acdb"),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
