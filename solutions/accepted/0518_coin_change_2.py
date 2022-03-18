#!/usr/bin/env python3
# 518. Coin Change 2
# https://leetcode.com/problems/coin-change-2/

# Medium

# Accepted
# Result: https://leetcode.com/submissions/detail/660749421/
# Time: 177ms (83.53%)
# Mem: 13.9MB (92.24%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 
class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def loop(i, a):
            if (i,a) in self.memo: #return cache
                return self.memo[(i,a)]
            if a == amount: #sum matches amount
                return 1
            if a > amount or i == len(coins): #out of bounds
                return 0
            
            self.memo[(i,a)] = loop(i, a+coins[i]) + loop(i+1, a) #try both cases, new coin, same sum or same coin with new sum
            return self.memo[(i,a)]
        
        self.memo = {}
        return loop(0,0)


#faster
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        table = [0] * (amount+1) #dp table
        
        table[0] = 1 #base case
        
        for coin in coins: #loop through coins
            for total in range(coin, amount+1): #loop through coins vals to amount
                table[total] += table[total-coin] #update val total
        return table[-1] #return the last item


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (5, [1,2,5]),
                (3, [2]),
                (10, [10], 1),


                ):

            funct = inspect.getmembers(f)[-1][1]

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct, e[-1], *e[:-1])
            timer(funct, 5, *e[:-1])


            print()
