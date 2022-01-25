#!/usr/bin/env python3
# 938. Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/627680493/
# Time: 292ms (31.81%)
# Mem: 22.1MB (97.26%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root == None:
            return 0
        elif root.val < low or root.val > high:
            root.val = 0
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


if __name__ == "__main__":
    pass

