#!/usr/bin/env python3
# 1684. Count the Number of Consistent Strings
# https://leetcode.com/problems/count-the-number-of-consistent-strings/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/626862686/
# Time: 260ms (61.69%)
# Mem: 16.2MB (63.02%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        result = 0
        for word in words:
            word = set(word)
            result += 1 if word & allowed == word else 0
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
                ("ab", ["ad","bd","aaab","baa","badab"], 2),
                ("abc", ["a","b","c","ab","ac","bc","abc"], 7),
                ("cad", ["cc","acd","b","ba","bac","bad","ac","d"], 4),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
