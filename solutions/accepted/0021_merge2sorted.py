#!/usr/bin/env python3
#21. Merge Two Sorted Lists
# EASY
# https://leetcode.com/problems/merge-two-sorted-lists/
# Accepted!
# 40ms-44ms??? (30.41%)
#14.4 MB (86.70%)
# https://leetcode.com/submissions/detail/595070915/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# HELPERS
def load_node(vals=[], node=None):
    if vals:
        node = ListNode(vals.pop(0))
        if vals:
            node.next = load_node(vals, node)
    return node

def unload_node(node=None):
    results = []
    while node:
        results.append(node.val)
        node = node.next
    return results

def print_node(node):
    pnode = node
    while pnode is not None:
        print(pnode.val)
        pnode = pnode.next


class Solution:

    head = None
    
    def at_end(self, val):
        node = ListNode(val)
        if self.head == None:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node


    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        while l1 != None or l2 != None:
            if l2 != None and l1 == None:
                self.at_end(l2.val)
                l2 = l2.next
            elif l1 and not l2:
                self.at_end(l1.val)
                l1 = l1.next
            elif l1.val <= l2.val:
                self.at_end(l1.val)
                l1 = l1.next
            elif l2.val < l1.val:
                self.at_end(l2.val)
                l2 = l2.next
        return self.head


if __name__ == "__main__":
    for ex in (
            ([0,1,2,4], [1,3,4], [0,1,1,2,3,4,4]),
            ([1,2,4,5,6,8,21], [9, 13, 22], [1,2,4,5,6,8,9,13,21,22]),
            ([1,2,4,5,6,8,21,23,50], [9, 13, 22], [1,2,4,5,6,8,9,13,21,22,23,50]),
            ):

        l1 = load_node(ex[0].copy())
        l2 = load_node(ex[1].copy())
        l3 = Solution().mergeTwoLists(l1, l2)
        result = unload_node(l3)
        print(ex[0], ex[1], "PASS" if result == ex[2] else "FAIL")
