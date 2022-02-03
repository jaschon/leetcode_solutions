#!/usr/bin/env python3
# 100. Same Tree
# https://leetcode.com/problems/same-tree/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/633786874/
# Time: 40ms (44.35%)
# Mem: 14MB (92.97%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# First make exits!
# 1. return if both p and q are out of nodes (Null)
# 2. return false if one node is out and the other has a node
# 3. return false if values don't match
# Next keep 'cursing left sides and right sides and return the values when they exit
# 4. return a recursive loop left sides AND recursive loop right sides

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not q or not p:
            return False
        elif p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)


if __name__ == "__main__":
    pass

