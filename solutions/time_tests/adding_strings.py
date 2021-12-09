#!/usr/bin/env python3


import sys
sys.path.insert(0,'..')
from _helper import *


class Solution:
    def test(self, n):
        """ADD"""
        return n+"b"

class Solution2:
    def test(self, n):
        return f"{n}b"

if __name__ == "__main__":
    for f in ( 
            Solution().test, 
            Solution2().test,
            ):
        for e in (
                ("a", "ab"),
                ("aaaaa", "aaaaab"),

                ):

            funct = f

            print()
            test(funct, e[1], e[0])
            timer(funct, e[0])
            print()

