#!/usr/bin/env python3
# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/652724869/
# Time: 41ms (56.35%)
# Mem: 14MB (59.01%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class MyQueue:

    def __init__(self):
        self.q = []
        

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        return self.q.pop(0)
        

    def peek(self) -> int:
        return self.q[0]
        

    def empty(self) -> bool:
        return len(self.q) == 0



if __name__ == "__main__":
    pass

