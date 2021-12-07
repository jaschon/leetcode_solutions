#!/usr/bin/env python3
# https://leetcode.com/problems/reverse-string/
# 344. Reverse String
# Easy

# Accepted!
# Result: https://leetcode.com/submissions/detail/598540471/
# Time: 188ms (96.72%)
# Mem: 18.8MB (18.58%)

import sys
sys.path.insert(0,'..')
from _helper import *


class Solution:
    def reverseString(self, s: list[str]) -> None:
        for i in range(1, (len(s)//2)+1):
            s[i-1], s[-i] = s[-i], s[i-1]

if __name__ == "__main__":
    for e in (
            (["h","e","l","l","o"], ["o","l","l","e","h"]),
            (["J", "a", "s", "o", "n"], ["n", "o", "s", "a", "J"]),
            (["H","a","n","n","a","h"], ["h","a","n","n","a","H"]),
            (["a"], ["a"]),
            ([], []),
            (["1", "2", "3"], ["3", "2", "1"]),
            (["1", "2"], ["2", "1"]),
            (["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"], ["a","m","a","n","a","P"," ",":","l","a","n","a","c"," ","a"," ",",","n","a","l","p"," ","a"," ",",","n","a","m"," ","A"]),


            ):

        funct = Solution().reverseString

        print()

        test(funct, e[1], e[0])
        timer(funct, e[0])

        print()
