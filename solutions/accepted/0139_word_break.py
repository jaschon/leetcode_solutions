#!/usr/bin/env python3
# 139. Word Break
# https://leetcode.com/problems/word-break/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/642683205/
# Time: 40ms (80.78%)
# Mem: 14.1 MB (75.18%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    
    def __init__(self):
        self.memo = {}
        
    def wordBreak(self, s, wordDict):
        if s in self.memo:
            return self.memo[s]
        if s == "":
            return True

        for word in wordDict:
            if s.startswith(word) == True:
                if self.wordBreak(s[len(word):], wordDict) == True:
                    self.memo[s] = True
                    return True

        self.memo[s] = False
        
        return False


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                # ("leetcode", ["leet","code"], {}, True),
                ("a", ["b"], False),
                # ("cars", ["car", "ca", "rs"], {}, True),
                # ("catsandog", ["cats","dog","sand","and","cat"], {}, False),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
