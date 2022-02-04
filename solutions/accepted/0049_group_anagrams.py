#!/usr/bin/env python3
# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/633945847/
# Time: 92ms (95.11%)
# Mem: 17.2MB (79.43%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

# take each word and make a sorted key
# if found in dict add it to the end of value array or create new key with word in an array

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        match = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in match:
                match[key].append(word)
            else:
                match[key] = [word,]
        return list(match.values())


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
                ([""], [[""]]),
                (["a"], [["a"]]),


                ):

            # funct = inspect.getmembers(f)[-1][1]
            funct = Solution().groupAnagrams

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
