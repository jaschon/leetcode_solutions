#!/usr/bin/env python3

import timeit

# Linked List Helpers
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

# Pass Fail
def test(funct, cmp, *val):
    result = funct(*val)
    print("TEST:", "--OK--" if result == cmp else "--FAIL--")
    print("IN:", val)
    print("OUT:", result)
    print("EXPECTED:", cmp)

def timer(funct, *param):
    t = timeit.Timer(lambda: funct(*param))
    print("TIMER:", t.timeit(5))

