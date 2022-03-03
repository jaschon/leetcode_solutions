#!/usr/bin/env python3
# 589. N-ary Tree Preorder Traversal
# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/652661745/
# Time: 63ms (65.45%)
# Mem: 16.3MB (10.60%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def loopy(node, result):
            if node == None: 
                return
            result.append(node.val)
            for c in node.children:
                loopy(c, result)
            return result
        return loopy(root, [])
        



if __name__ == "__main__":
    pass

