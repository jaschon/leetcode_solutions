#!/usr/bin/env python3
# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/655929856/
# Time: 32ms (87.58%)
# Mem: 13.9MB (44.72%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
                



if __name__ == "__main__":
    pass

