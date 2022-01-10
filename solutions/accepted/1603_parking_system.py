#!/usr/bin/env python3
# 1603. Design Parking System
# https://leetcode.com/problems/design-parking-system/

# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/617031243/
# Time: 152ms (30.04%)??
# Mem: 14.7MB (81.44%)??

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

class ParkingSystem:

    lot = {}

    def __init__(self, big: int, medium: int, small: int):
        self.lot[1] = [big,0]
        self.lot[2] = [medium,0]
        self.lot[3] = [small,0]

    def addCar(self, carType: int) -> bool:
        self.lot[carType][1] += 1
        return self.lot[carType][0] > 0 and self.lot[carType][1] <= self.lot[carType][0]
        

if __name__ == "__main__":
    pass
