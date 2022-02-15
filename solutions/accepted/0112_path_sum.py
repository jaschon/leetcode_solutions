#!/usr/bin/env python3
# 112. Path Sum
# https://leetcode.com/problems/path-sum/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/641432873/
# Time: 52ms (58.06%)
# Mem: 15.1MB (38.85%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List

# Steps
# Basic recurs tree function
# 1 - return False if root is not a node
# 2 - return if leaf found (doesn't have a left for right node) and targetsum == node sum
# 3 - return recurs using left and right nodes. subtract current node value from target sum each time.

### ADD SOLUTION CLASS HERE 
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        if root.left == None and root.right == None:
            return targetSum == root.val

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
        



if __name__ == "__main__":
    pass

