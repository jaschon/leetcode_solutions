#!/usr/bin/env python3
# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/

# Easy

# Accepted
# Result: 
# Time:
# Mem:

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# 1. make a dummy node (for result)
# 2. set prev to the dummy and current to the head node
# 3. loop while current
# 4  store current.next in a tmp var
# 5. if current is the val we need, set prev.next to tmp, else prev = current
# 6. set current to tmp
# 7. return result.next when current hits the end

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        
        result = ListNode(next=head)
        
        prev, current = result, head
        
       
        while current:
                       
            tmp = current.next
            
            if current.val == val:
                prev.next = tmp
            else:
                prev = current
                
            current = tmp
                
                
        return result.next



if __name__ == "__main__":
    pass

