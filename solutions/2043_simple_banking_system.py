#!/usr/bin/env python3
# 2043. Simple Bank System
# https://leetcode.com/problems/simple-bank-system/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/627070862/
# Time: 755ms (49.14%)
# Mem: 43.7MB (74.36%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 <= len(self.balance) >= account2 and self.balance[account1-1] - money >= 0:
                self.balance[account2-1] += money
                self.balance[account1-1] -= money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account <= len(self.balance):
            self.balance[account-1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account <= len(self.balance) and self.balance[account-1] - money >= 0:
            self.balance[account-1] -= money
            return True
        return False


if __name__ == "__main__":
    pass
 
