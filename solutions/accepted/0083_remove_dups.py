#!/usr/bin/env python3
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# 83. Remove Duplicates from Sorted List
# Easy

# Accepted! 
# Result: https://leetcode.com/submissions/detail/597952367/
# Time: 40ms (82.22%)
# Mem: 14.4MB (25.43%)

import sys
sys.path.insert(0,'..')
from _helper import *

class Solution:
    def deleteDuplicates(self, head=None):
        start = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return start
        
if __name__ == "__main__":
    for e in (
            ([], []),
            ([1,1,2], [1,2]),
            ([1,1,1], [1]),


            ):

        funct = Solution().deleteDuplicates

        print()

        test_node(funct, e[1], e[0])
        timer(funct, load_node(e[0]))

        print()
