#!/usr/bin/env python3
# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/655353254/
# Time: 42ms (67.35%)
# Mem: 14.1MB (53.36%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        def check(left, right):
            
            if left == None and right == None:
                return True
            elif right == None or left == None:
                return False
            
            return left.val == right.val \
                and check(left.left, right.right) \
                and check(left.right, right.left)

            
        if root == None:
            return True
        return check(root.left, root.right)



if __name__ == "__main__":
    pass

