#!/usr/bin/env python3
# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/655379542/
# Time: 45ms (62.58%)
# Mem: 14.2MB (91.33%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# BFS!
# 1. make queue and result list
# 2. add root to queue
# 3 while q
# a. make tmp list to store row items
# b. loop through q
# c. get node
# d. if node is not null, add the value to row list and add both left/right children to queue
# e. if row has values, add them to the result list
# f. while loop exits, so return result list


from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        q = deque()
        q.append(root)
        
        while q:
            qlen = len(q)
            row = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    row.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if row:
                result.append(row)
            
        return result



if __name__ == "__main__":
    pass

