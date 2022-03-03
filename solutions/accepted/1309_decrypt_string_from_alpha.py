#!/usr/bin/env python3
# 1309. Decrypt String from Alphabet to Integer Mapping
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/652746266/
# Time: 64ms (13.20%)
# Mem: 13.9MB (84.65%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = ""
        mapper = { 
                '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
                '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10#': 'j',
                '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n',
                '15#': 'o', '16#': 'p', '17#': 'q', '18#': 'r',
                '19#': 's', '20#': 't', '21#': 'u', '22#': 'v', '23#': 'w',
                '24#': 'x', '25#': 'y', '26#': 'z',
                }
        i = 0
        while i < len(s):
            tmp = mapper.get(s[i])
            try:
                if s[i+2] == "#":
                    tmp = mapper.get(s[i:i+3])
                    i += 2
            except:
                pass
            i += 1
            result += tmp
        return result

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("10#11#12", "jkab"),
                ("1326#", "acz"),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
