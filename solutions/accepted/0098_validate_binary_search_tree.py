#!/usr/bin/env python3
# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/655372298/
# Time: 48ms (82.81%)
# Mem: 16.5MB (40.84%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(node, left_bound, right_bound):
            if not node:
                return True
            
            if not (node.val < right_bound and node.val > left_bound):
                return False
            
            return check(node.left, left_bound, node.val) and check(node.right, node.val, right_bound)
        
        
        return check(root, float("-inf"), float("inf"))




if __name__ == "__main__":
    pass

