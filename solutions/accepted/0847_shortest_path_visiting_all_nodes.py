#!/usr/bin/env python3
# 847. Shortest Path Visiting All Nodes
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/

# Hard

# Accepted
# Result: 
# Time:
# Mem:

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

# keep track of which nodes you visited by a bitmask (like a check list)

# main loop
# make a bitmask (checklist) of all 1's
# set up memo and graph
# loop through all nodes and run loop, returning the smallest answer


# loop, standard DP!
# 1. return if found in memo
# 2. return 0 if loop reached the end and only seen one node
# 3. set memo for that key to a really large number, incase it returns without finding anything

# 4. loop through all nodes and count
# a. if you visited it (1 + loop(node index) )
# b. if you didn't ( 1 + loop(node index, not mask (1 << node index))
# 5. set memo to the smallest value in visited vs not visited vs cached
# 6. return whatever is set in memo


class Solution:

    def _loop(self, index, mask):
        
        key = (index, mask)
        if key in self.memo:
            return self.memo[key]

        if mask & (mask-1) == 0:
            return 0

        self.memo[key] = float("inf")

        for g in self.graph[index]:
            if mask & (1 << g):
                vis = 1 + self._loop(g, mask)
                n_vis = 1 + self._loop(g, mask ^ (1 << index))
                self.memo[key] = min(self.memo[key], vis, n_vis)

        return self.memo[key]



    def shortestPathLength(self, graph: List[List[int]]) -> int:



        length = len(graph)
        mask = (1<< len(graph)) - 1
        self.memo = {}
        self.graph = graph

        return min(self._loop(i, mask) for i in range(len(graph)))





if __name__ == "__main__":
    pass

