#!/usr/bin/env python3
# 140. Word Break II
# https://leetcode.com/problems/word-break-ii/

# Hard

# Accepted
# Result: https://leetcode.com/problems/word-break-ii/submissions/
# Time: 28ms (93.43%)
# Mem: 13.9MB (94.90%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

# like break 1, but return the combos
# loop through worddict, if s matches start of word, 
# - add it to combos...
# - pass to recurs with results, combos and s with the word remove from the front
# - if it finally hits s == '', you know it fully matches so you can add combos to result
# - remove the last index of combos

class Solution:
    def wordBreak(self, s, wordDict):
        if not wordDict: return []
        combination = []
        results = []
        self._loopy(results, wordDict, combination, s)
        return results
    def _loopy(self, results, wordDict, combination, s):
        if s == "": 
            results.append(" ".join(combination))
            return
        for word in wordDict:
            if s.startswith(word) == True:
                combination.append(word)
                self._loopy(results, wordDict, combination, s[len(word):])
                combination.pop()



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("catsanddog", ["cat","cats","and","sand","dog"], ["cats and dog","cat sand dog"]),
                # ("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"], ["pine apple pen apple","pineapple pen apple","pine applepen apple"]),
                # ("catsandog", ["cats","dog","sand","and","cat"], []),
                ("aaaaaaa", ["aaaa","aa","a"], ["a a a a a a a","aa a a a a a","a aa a a a a","a a aa a a a","aa aa a a a","aaaa a a a","a a a aa a a","aa a aa a a","a aa aa a a","a aaaa a a","a a a a aa a","aa a a aa a","a aa a aa a","a a aa aa a","aa aa aa a","aaaa aa a","a a aaaa a","aa aaaa a","a a a a a aa","aa a a a aa","a aa a a aa","a a aa a aa","aa aa a aa","aaaa a aa","a a a aa aa","aa a aa aa","a aa aa aa","a aaaa aa","a a a aaaa","aa a aaaa","a aa aaaa"]),


                ):

            # funct = inspect.getmembers(f)[-1][1]
            funct = f.wordBreak

            print()

            # test_node(funct, e[-1], *e[:-1])

            test_list(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
