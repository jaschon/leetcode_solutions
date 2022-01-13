#!/usr/bin/env python3
# 804. Unique Morse Code Words
# https://leetcode.com/problems/unique-morse-code-words/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/619112294/
# Time: 36ms (71.94%)
# Mem: 14.3MB (30.90%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {'a':".-", 'b':"-...", 'c': "-.-.", 'd': "-..",
                 'e': ".", 'f': "..-.", 'g': "--.", 'h': "....",
                 'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..",
                 'm': "--", 'n': "-.", 'o': "---", 'p': ".--.",
                 'q': "--.-", 'r': ".-.", 's': "...", 't': "-",
                 'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-",
                 'y': "-.--", 'z': "--.."}
        result = set()
        for word in words:
            result.add("".join(morse[c] for c in word))
        return len(result)

        



if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (["gin","zen","gig","msg"], 2),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
