#!/usr/bin/env python3
# 2109. Adding Spaces to a String
# https://leetcode.com/problems/adding-spaces-to-a-string/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/613809268/
# Time: 1610ms (5.28%)
# Mem: 51.8MB (40.08%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# Fastest, but times out!
class Solution3:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        result[:0] = s
        for i, n in enumerate(spaces):
            n += i
            result.insert(n, " ")
        return "".join(result)

class Solution4:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = list(s)
        for i, n in enumerate(spaces):
            result.insert(n+i, " ")
        return "".join(result)


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ""
        counter = 0
        length = len(spaces)
        for i, ch in enumerate(s):
            if counter < length and spaces[counter] == i:
                counter += 1
                result += " "
            result += ch
        return result

class Solution2:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        counter = 0
        length = len(spaces)
        for i, ch in enumerate(s):
            if counter < length and spaces[counter] == i:
                counter += 1
                result.append(" ")
            result.append(ch)
        return "".join(result)


class Solution5:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s = list(s)
        for i, n in enumerate(spaces):
            s[i] = " " + s[i]
        return "".join(s)


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            # Solution(),
            # Solution2(),
            Solution3(),
            Solution4(),
            Solution5(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                # ("LeetcodeHelpsMeLearn", [8,13,15], "Leetcode Helps Me Learn"),
                # ("icodeinpython", [1,5,7,9], "i code in py thon"),
                ("spacing", [0,1,2,3,4,5,6], " s p a c i n g"),

                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
