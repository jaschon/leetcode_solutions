#!/usr/bin/env python3
# 1288. Remove Covered Intervals
# https://leetcode.com/problems/remove-covered-intervals/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/651431017/
# Time: 108ms (78.97%)
# Mem: 14.5MB (55.31%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# 1. sort points! smaller x, then largest y
# 2. add the first item to the results list
# 3. loop through list and compare item to last item in results
# if item x is greater than last result x and item y is less than last result y, skip
# else add to results
# 4. return length of results


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: (x[0], -x[1]))

        result = [intervals[0]]

        for i in intervals[1:]:
            if result[-1][0] <= i[0] and result[-1][1] >= i[1]:
                continue
            result.append(i)

        return len(result)



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([[1,4],[3,6],[2,8]], 2),
                ([[1,4],[2,3]], 1),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
