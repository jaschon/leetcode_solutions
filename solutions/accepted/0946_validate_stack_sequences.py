#!/usr/bin/env python3

# 946. Validate Stack Sequences
# https://leetcode.com/problems/validate-stack-sequences/
# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/661216437/
# Time: 92 ms (64.33%)
# Mem: 14.1MB (93.97%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# greedy! add items to stack, then while loop remove them

# 1. get length of pushed
# 2. set up stack and counter

# 3. loop through pushed
# 4. add item to stack
# 5  while loop stack and check if the last item in stack matches the counter index of popped
# 6. if so, pop and add counter

# 7. counter of popped items should match length of pushed



class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        length = len(pushed)
        
        stack = []
        
        count = 0
        
        for item in pushed:
            
            stack.append(item)
            
            while stack and count < length and stack[-1] == popped[count]:
                stack.pop()
                count += 1
                
                
        return count == length


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ([1,2,3,4,5], [4,5,3,2,1], True),
                ([1,2,3,4,5], [4,3,5,1,2], False),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
