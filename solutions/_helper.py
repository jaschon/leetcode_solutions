#!/usr/bin/env python3

import timeit

# Linked List Helpers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
def print_test(funct, result, test, cmp, *val):
    print(f">> {funct.__qualname__} ({funct.__doc__ or '-'})")
    print("TEST:", "--OK--" if test == True else "--FAIL--")
    print("IN:", val)
    print("OUT:", result)
    print("EXPECTED:", cmp)

def test(funct, cmp, *val):
    result = funct(*val)
    print_test(funct, result, cmp == result, cmp, *val)

def test_node(funct, cmp, val):
    test(funct, cmp, load_node(val))

def test_list(funct, cmp, *val):
    result = funct(*val)
    length_test = len(cmp) == len(result)
    match_test = True
    for r in result:
        if not r in cmp:
            match_test = False
            break
    print_test(funct, result, match_test and length_test, cmp, *val)
    
# Timer
def timer(funct, amt, *param):
    t = timeit.Timer(lambda: funct(*param))
    print(f"TIMER ({amt}x):", f"{t.timeit(amt)}")
