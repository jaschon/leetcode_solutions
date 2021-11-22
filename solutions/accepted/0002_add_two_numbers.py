#!/usr/bin/env python3
# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
# Medium
# Accepted
# https://leetcode.com/problems/add-two-numbers/submissions/
# 72ms (58.57%)
# 14.3MB (73.60)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2, carry=0):
        total = l1.val+l2.val+carry
        carry = total//10
        node = ListNode(total % 10)
        if l1.next or l2.next or carry != 0:
            if l1.next == None: l1.next = ListNode(0)
            if l2.next == None: l2.next = ListNode(0)
            node.next = self.addTwoNumbers(l1.next, l2.next, carry)
        return node

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

if __name__ == "__main__":
    for ex in (
            ([2,4,3], [5,6,4], [7,0,8]),

            ):
        l1 = load_node(ex[0])
        l2 = load_node(ex[1])

        result = unload_node(Solution().addTwoNumbers(l1, l2))
        print(result, "PASS" if result == ex[-1] else "FAIL")


