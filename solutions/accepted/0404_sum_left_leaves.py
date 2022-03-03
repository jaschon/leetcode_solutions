#!/usr/bin/env python3
# 404. Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/652779192/
# Time: 52ms (39.41%)
# Mem: 14.8MB (31.36%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# 1. make an object var to hold sum
# 2. start loop and return total sum
# 3. in loop, exit if it is a null val
# 4. if it is a left side item, and has no left or right branches, add to total
# 5. check left and right sides

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def loopy(node, is_left=False):
            if not node:
                return
            if is_left and not node.left and not node.right: 
                self.sum += node.val
            loopy(node.left, True)
            loopy(node.right, False)
            
        self.sum = 0
        loopy(root, False)
        return self.sum   



if __name__ == "__main__":
    pass

