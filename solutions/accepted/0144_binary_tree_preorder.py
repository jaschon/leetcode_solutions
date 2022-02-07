#!/usr/bin/env python3
# 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Easy

# Accepted
# Result:  https://leetcode.com/submissions/detail/636729577/
# Time: 32ms (78.35%)
# Mem: 13.8MB (93.64%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def loopy(node, result):
            if node == None: 
                return
            result.append(node.val) #1) for preorder, append first
            loopy(node.left, result) #2 left
            loopy(node.right, result) #3 right
            return result #return
        return loopy(root, []) #start with the root
        



if __name__ == "__main__":
    pass

