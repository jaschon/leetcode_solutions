#!/usr/bin/env python3
# 2129. Capitalize the Title
# https://leetcode.com/problems/capitalize-the-title/

# Easy

# Accepted Solution 
# Result: https://leetcode.com/submissions/detail/619806247/
# Time: 32ms (87.14%)
# Mem: 14.2MB (76.16%)

# Accepted Solution 2
# Result: https://leetcode.com/submissions/detail/619808287/
# Time: 47ms (43.72%)
# Mem: 14.1 MB (93.09%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        result = []
        for word in title.split():
            if len(word) > 2:
                result.append(word.title())
            else:
                result.append(word.lower())
        return " ".join(result)

class Solution2:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join(map(lambda x: x.lower() if len(x) < 3 else x.title(), title.split()))

class Solution3:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join([word.lower() if len(word) < 3 else word.title() for word in title.split()])

class Solution4:
    def capitalizeTitle(self, title: str) -> str:
        
        s = ""
        for word in title.split():
            if len(word) < 3:
                s += word.lower() + " "
            else:
                word = word.lower()
                s += chr(ord(word[0]) - 32) + word[1:] + " "
                    
        return s[:-1]

if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            Solution2(),
            Solution3(),
            Solution4(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                ("capiTalIze tHe titLe", "Capitalize The Title"),
                ("First leTTeR of EACH Word", "First Letter of Each Word"),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
