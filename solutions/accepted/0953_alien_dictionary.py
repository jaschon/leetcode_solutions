#!/usr/bin/env python3
# 953. Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/652766444/
# Time: 48ms (60.33%)
# Mem: 13.9MB (93.78%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
# 1. make map of chars to digits
# 2. loop through words
# 3. loop through chars in word
# 4. if length of current is larger than len of next word, fail
# 5. check if char in word is not the same as char in next word
# if so, check if the mapped is greater, if so, fail
# return true if everything passes

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapper = { key : val+1 for val, key in enumerate(order) }
        for word in range(len(words)-1):
            for char in range(len(words[word])):
                if char >= len(words[word+1]): return False
                if words[word][char] != words[word+1][char]:
                    if mapper[words[word][char]] > mapper[words[word+1][char]]:
                            return False
                    break
        return True

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
                (["apap","app"], "abcdefghijklmnopqrstuvwxyz", True),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
