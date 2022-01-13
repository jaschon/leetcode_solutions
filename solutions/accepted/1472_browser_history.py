#!/usr/bin/env python3
# 1472. Design Browser History
# https://leetcode.com/problems/design-browser-history/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/619171926/
# Time: 220ms (86.78%)
# Mem: 16.6 MB (60.97%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage,]
        self.place = 0
      
    def visit(self, url: str) -> None:
        self.history = self.history[:self.place+1]
        self.history.append(url)
        self.place = len(self.history)-1
        

    def back(self, steps: int) -> str:
        amt = self.place - steps
        self.place = 0 if amt < 0 else amt
        return self.history[self.place]


    def forward(self, steps: int) -> str:
        amt = self.place + steps
        self.place = len(self.history)-1 if amt > len(self.history)-1 else amt
        return self.history[self.place]


if __name__ == "__main__":
    e = ["BrowserHistory","visit","forward","back","visit","visit","visit","visit","back","visit","back","forward","visit","visit","visit"]
    p = ["hdqqhm.com","yltqtsj.com",1,1,"cyv.com","vbpvni.com","opy.com","kbyzp.com",7,"fchhxaz.com",6,9,"rg.com","oemqn.com","hyqsb.com"]
    expected = [None,None,"yltqtsj.com","hdqqhm.com",None,None,None,None,"hdqqhm.com",None,"hdqqhm.com","fchhxaz.com",None,None,None]
    result = []
    for i in range(len(e)):
        m = e[i]
        if m == "BrowserHistory":
            s = BrowserHistory(p[i])
            result.append(None)
        elif m == "visit":
            result.append(s.visit(p[i]))
        elif m == "back":
            result.append(s.back(p[i]))
        elif m == "forward":
            result.append(s.forward(p[i]))
        print("-OK-" if result[i] == expected[i] else "-FAIL-", f'{m=}', f'{p[i]=}', f'{result[i]=}', f'{expected[i]=}', f'{s.history=}')
    print(result)
    print(expected)

    
