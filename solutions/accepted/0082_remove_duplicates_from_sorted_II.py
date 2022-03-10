#!/usr/bin/env python3
# 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/656620076/
# Time: 50ms (67.62%)
# Mem: 13.9MB ( 54.61%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

# VARS
# - start stores the top of the list
# - end stores the current tail
# - head stores the position we are checking

# CODE
# -- loop through head

# - if current head finds a value that matches the next value in head
# - loop through head until it doesn't match
# - then attach the end to head (end.next = head.next)

# - else, move end up to end.next

# -- move head up before looping....

# --- when you exit the loop, return the start.next (the top of the list)



class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        start = end = ListNode(next=head)
        
        while head:
            
            if head.next and head.val == head.next.val:
                
                while head.next and head.val == head.next.val:
                    head = head.next
                    
                end.next = head.next
                
            else:
                end = end.next
                
            head = head.next
            
        return start.next



if __name__ == "__main__":
    pass

