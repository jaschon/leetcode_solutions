#!/usr/bin/env python3


import sys
sys.path.insert(0,'..')
from _helper import *


class Solution:
    """SLASH"""
    def test(self, n):
        return n//3

class Solution2:
    def test(self, n):
        """INT"""
        return int(n/3)
        
class Solution3:
    """SLASH SAVE"""
    def test(self, n):
        s = n//3
        return s


if __name__ == "__main__":

    for f in ( 
            Solution().test, 
            Solution2().test,
            Solution3().test,
            ):
        for e in (
            (10,3),
            (100, 33),
            (1000, 333),
            (10000, 3333),
            (100000, 33333),

                ):

            funct = f

            print()
            test(funct, e[1], e[0])
            timer(funct, e[0])
            print()

