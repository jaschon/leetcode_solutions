#!/usr/bin/env python3
# 700. Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/655389836/
# Time: 200ms (5.27%)
# Mem: 16.5MB (45.42%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root == None:
            return None
        if root.val == val:
            return root
        
        return self.searchBST(root.left, val) or self.searchBST(root.right, val)



if __name__ == "__main__":
    pass

