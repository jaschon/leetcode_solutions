#!/usr/bin/env python3
# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/641313430/
# Time: 66ms (48.96%)
# Mem: 16.3 MB (18.15%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# 1 - return 0 if root is null
# 2 - plus 1 every level

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == "__main__":
    pass

