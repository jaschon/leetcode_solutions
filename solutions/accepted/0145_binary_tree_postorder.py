#!/usr/bin/env python3
# 145. Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/636730197/
# Time: 54ms (18.96%)
# Mem: 13.8MB (93.75%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def loopy(node, result):
            if node == None: 
                return
            loopy(node.left, result) #1 left
            loopy(node.right, result) #2 right
            result.append(node.val) # 3) add to var last
            return result #return
        return loopy(root, []) #start with root and return  



if __name__ == "__main__":
    pass

