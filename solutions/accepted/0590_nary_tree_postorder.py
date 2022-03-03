#!/usr/bin/env python3
# 590. N-ary Tree Postorder Traversal
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/652662934/
# Time: 97ms (14.87%)
# Mem: 16.2MB (27.60%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def loopy(node, result):
            if node == None: 
                return
            for c in node.children:
                loopy(c, result)
            result.append(node.val)
            return result
        return loopy(root, [])  



if __name__ == "__main__":
    pass

