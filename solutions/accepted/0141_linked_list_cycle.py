#!/usr/bin/env python3

# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/submissions/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/653343903/
# Time: 60ms (79.01%)
# Mem: 17.7MB (44.78%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

# fast/slow method again!
# -> fast moves twice as fast. 
# -> if it reaches the end, no loop. 
# -> if it finds slow, it must be a loop

# 1. slow and fast are set to head
# 2. while fast and fast.next
# 3. set slow to the next node
# 4. set fast to 2 nodes ahead
# 5 if fast reaches the end, it can't be a loop
# 6. if fast hits slow, it must have looped back and it is a loop


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = head
        
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
            
            if fast == None:
                return False
            if slow == fast:
                return True
            
        return False



if __name__ == "__main__":
    pass

