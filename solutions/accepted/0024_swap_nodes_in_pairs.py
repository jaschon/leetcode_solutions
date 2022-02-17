#!/usr/bin/env python3
# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Medium

# Accepted
# Result: https://leetcode.com/problems/swap-nodes-in-pairs/submissions/
# Time: 35ms (63.47%)
# Mem: 13.7MB (99.98%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# make a new head node and store next as the head node param (this holds the top of the list)
# set a loop var current and start it at the head node
# loop until next or next.next is null
# hold next and next.next in tmp vars
# swap next and next.next
# set current to current.next.next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(next=head)
        current = result
        while current.next != None and current.next.next != None:

            first = current.next
            second = current.next.next

            first.next = second.next

            current.next = second

            current.next.next = first

            current = current.next.next

        return result.next


if __name__ == "__main__":
    pass

