#!/usr/bin/env python3
# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/648148399/
# Time: 24ms (97.56%)
# Mem: 13.9MB (87.49%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE
# slow, fast trick
# when fast reaches the end, slow should be in the middle

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow



if __name__ == "__main__":
    pass

