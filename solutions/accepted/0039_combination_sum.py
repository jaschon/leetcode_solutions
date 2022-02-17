#!/usr/bin/env python3
# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

# Medium

# Accepted
# Result: https://leetcode.com/problems/combination-sum/submissions/ 
# Time: 52ms (97.44%)
# Mem: 14MB (87.78%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        if not candidates: return []

        combination = []
        candidates.sort()
        results = []

        self._loopy(results, candidates, combination, target, 0)

        return results

    def _loopy(self, results, candidates, combination, target, start):

        if target == 0:
            results.append(list(combination))
            return

        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break

            combination.append(candidates[i])

            self._loopy(results, candidates, combination, target-candidates[i], i)

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
                ([2,3,6,7], 7, [[2,2,3],[7]]),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test_list(funct, e[-1], *e[:-1])
            # timer(funct, 5, *e[:-1])


            print()
