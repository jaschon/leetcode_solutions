#!/usr/bin/env python3

# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/653363703/
# Time: 46ms (63.63%)
# Mem: 15.4MB (74.23%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, current = None, head
        
        
        while current:
            
            tmp = current.next
            
            current.next = prev
            prev = current
            current = tmp
            
        return prev



if __name__ == "__main__":
    pass

