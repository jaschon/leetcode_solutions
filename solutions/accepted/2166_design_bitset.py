#!/usr/bin/env python3
# 2166. Design Bitset
# https://leetcode.com/problems/design-bitset/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/638065495/
# Time: 640ms (99.46%)
# Mem: 46.5MB (30.34%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class Bitset:
    def __init__(self, size: int):
        self.bitset = ['0']*size
        self.flipped = ['1']*size #easier to use a reversed copy
        self.size = size
        self.counter = 0

    def fix(self, idx: int) -> None:
        if self.bitset[idx] == '0': #this tripped me up. can't inc counter if it is already a 1
            self.counter += 1
        self.bitset[idx] = '1'
        self.flipped[idx] = '0'
        
    def unfix(self, idx: int) -> None:
        if self.bitset[idx] == '1': #can't dec counter if already a 0
            self.counter -= 1
        self.bitset[idx] = '0'
        self.flipped[idx] = '1'

        
    def flip(self) -> None:
        self.counter = self.size - self.counter #counter is the opp
        self.bitset, self.flipped = self.flipped, self.bitset #swap flipped and bitset
        
    def all(self) -> bool:
        return self.counter == self.size

    def one(self) -> bool:
        return self.counter > 0
               
    def count(self) -> int:
        return self.counter
        
    def toString(self) -> str:
        return "".join(self.bitset) #just need to join string the bitset


if __name__ == "__main__":
    pass

