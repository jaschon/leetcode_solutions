#!/usr/bin/env python3
# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/633772082/
# Time: 32ms (77.45%)
# Mem: 13.9 MB (90.90%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

# traverse tree by
# 1. send root to recursive sub function
# 2. check if root is not null and "make sandwiches"
#   - send left to recursive function
#   - get value of current root
#   - send right to recursive function
# 3. return result

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def loopy(root):
            if root != None:
                loopy(root.left)
                result.append(root.val) #tree sandwich (all recursive function on both sides. value in the middle)
                loopy(root.right)
        loopy(root)
        return result




if __name__ == "__main__":
    pass

