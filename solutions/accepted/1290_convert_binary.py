#!/usr/bin/env python3
# 1290. Convert Binary Number in a Linked List to Integer
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Easy

# Accepted (Solution 2)
# Result: https://leetcode.com/submissions/detail/614347387/
# Time: 40ms (32.15%)
# Mem: 13.8 (100%)

# Accepted (Solution)
# Result: https://leetcode.com/submissions/detail/614350958/
# Time: 24ms (97.39)
# Mem: 14.3MB (37.34%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution2:
    def getDecimalValue(self, head: ListNode) -> int:
        result = f'0b{head.val}'
        while head.next:
            head = head.next
            result += f'{head.val}'
        return int(result, 2)

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = head.val
        while head.next:
            head = head.next
            result = (2*result) + head.val
        return result

class Solution3:
    def getDecimalValue(self, head: ListNode) -> int:
        result = head.val
        while head.next:
            head = head.next
            result = 2*result + head.val
        return result

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (load_node([1,0,1]), 5),
                (load_node([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]), 18880),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
