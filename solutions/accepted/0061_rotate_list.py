#!/usr/bin/env python3
# 61. Rotate List
# https://leetcode.com/problems/rotate-list/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/657980987/
# Time: 43ms (72.49%)
# Mem: 13.9 MB (82.24%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
        
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        #exit if empty head
        if not head:
            return head
        
        
        tail = head
        length = 1
        
        #find end and length
        while tail.next:
            tail = tail.next
            length +=1
        
        #keep k in bounds
        k = k % length
        
        #nothing to do if k is 0
        if k == 0:
            return head
        
        
        current = head
        
        #find the pos to snip
        for _ in range(length-k-1):
            current = current.next
        
        #the pos end is the new head
        result = current.next
        
        #new tail is current. make sure it ends Null
        current.next = None
        
        #attach the tail to the head
        tail.next = head
        
        return result
        



if __name__ == "__main__":
    pass

