#!/usr/bin/env python3
# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/659928488/
# Time: 466ms (75.24%)
# Mem: 21.8MB (88.42%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# 1. make dp grid
# 2. loop backwards between both
# 3a. if chars match set grid pos to 1 + diagonal val
# 3b. else set grid pos to the max of one to the right and one down
# 4. return the top of the grid 0,0

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
                    
        return dp[0][0]
                    

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("abcde", "ace", 3),
                ("abc", "abc", 3),
                ("abc", "def", 0),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
