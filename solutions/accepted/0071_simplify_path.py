#!/usr/bin/env python3
# 71. Simplify Path
# https://leetcode.com/problems/simplify-path/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/659862912/
# Time: 56ms (30.39%)
# Mem: 13.8MB (87.69%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = []
        for p in path.split("/"):
            if p == "..":
                if dirs:
                    dirs.pop()
            elif p != "." and p:
                dirs.append(p)
        return f"/{'/'.join(dirs)}"


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("/home/", "/home"),
                ("/../", "/"),
                ("/home//foo/", "/home/foo"),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
