#!/usr/bin/env python3
# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/647513132/
# Time: 36ms (93.59%)
# Mem: 14.3MB (91.72%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        mapper = {}

        def clone(node):
            if node in mapper: #return copy if found in mapper
                return mapper[node]
            
            #else
            #1 make copy of node
            #2 map node to copy
            #3 loop through node's neighbors and clone them to copy's neighbors
            #4 return copy
            copy = Node(node.val)
            mapper[node] = clone
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy
        #call clone on first node and test for empty test cases
        return clone(node) if node else None




if __name__ == "__main__":
    pass

