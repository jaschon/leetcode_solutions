#!/usr/bin/env python3
# 653. Two Sum IV - Input is a BST
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/655460005/
# Time: 83ms (87.05%)
# Mem: 16.2MB (99.66%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()
        q = deque()
        q.append(root)
        
        while q:
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    if k-node.val in visited:
                        return True
                    visited.add(node.val)
                    q.append(node.left)
                    q.append(node.right)           
        return False


if __name__ == "__main__":
    pass

