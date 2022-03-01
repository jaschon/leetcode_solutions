#!/usr/bin/env python3
# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

# Hard

# Accepted
# Result: https://leetcode.com/submissions/detail/651319861/
# Time: 120ms (77.45%)
# Mem: 17.6 MB (96.24%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# 1. while loop
# 2. take index i and index i+1 and send them to merge
# 3. append result back to temp array
# 4. set lists array to tmp array (so it will keep in the while loop

# easy merge sort

# 1. make an empty tail listnode
# 2. set your head node to tail (this keeps track of the top of the tail, which we return)

# 3. while loop left and right
# 4a. if left.val < right.val
# set tail.next to left
# set left position to left.next
# 4b. else
# set tail.next to right
# set right position to right.next

# 5. set tail to tail.next

# 6. dump extra left or right vals on tail.next

# 7. return head.next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            tmp = []
            for i in range(0, len(lists), 2):
                left = lists[i]
                try:
                    right = lists[i+1]
                except:
                    right = None
                tmp.append(self.merge(left, right))
            lists = tmp
        return lists[0]

    def merge(self, left, right):
        head = tail = ListNode()

        while left and right:

            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        if left:
            tail.next = left
        if right:
            tail.next = right

        return head.next

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
