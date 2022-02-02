#!/usr/bin/env python3
# 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/633272038/
# Time: 412ms (14.50%)
# Mem: 15.3MB (9.91%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lenp, lens = len(p), len(s)
        if lenp > lens: return []
        result = []
        #To stop a time out error,
        # build string counter to compare on the fly. 
        # add start char, compare strings counter
        # then remove it at the end of the loop.
        # also remove any 0 count items in string as well
        counter = Counter(p) #make a counter to compare
        strings = Counter(s[0:lenp-1]) #make a counter with out the first char of string. (we add it in the loop)
        for i in range(lens-lenp+1):
            strings[s[i+lenp-1]] += 1 # add the end char to the string counter
            if strings == counter:
                result.append(i)
            strings[s[i]] -= 1
            if strings[s[i]] == 0:
                del strings[s[i]]
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
                ("cbaebabacd", "abc", [0,6]),
                ("abab", "ab", [0,1,2]),
                ("acdcaeccde", "c", [1,3,6,7]),
                ("aaaaaaaaaa", "aaaaaaaaaaaaa", []),
                ("baa", "aa", [1]),
                ):

            # funct = inspect.getmembers(f)[-1][1]
            funct = f.findAnagrams

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
