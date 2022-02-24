#!/usr/bin/env python3

# 148. Sort List
# https://leetcode.com/problems/sort-list/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/648145356/
# Time: 485ms (54.34%)
# Mem: 29.9 MB (98.59%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head


        #split into 2 halves

        left = head
        right = self.get_middle(head)

        #break right from left
        holder = right.next
        right.next = None
        right = holder

        #sort each half
        left = self.sortList(left)
        right = self.sortList(right)

        #return merged
        return self.merge(left, right)


    def get_middle(self, head):
        # slow fast trick. 
        #fast reaches the end at the same point slow reaches the middle!

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right):

        tail = result = ListNode()

        # sort. add lesser val to tail until lists run out
        while left and right:

            if left.val < right.val:
                tail.next = left
                left = left.next

            else:
                tail.next = right
                right = right.next

            tail = tail.next

        # add any extras that didn't get added
        if left:
            tail.next = left
        if right:
            tail.next = right

        return result.next



if __name__ == "__main__":
    pass

