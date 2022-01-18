#!/usr/bin/env python3

# 1255. Maximum Score Words Formed by Letters
# https://leetcode.com/problems/maximum-score-words-formed-by-letters/

# Hard

# Accepted
# Result: https://leetcode.com/submissions/detail/622741156/
# Time: 576ms (11.07%)
# Mem: 14.5MB (18.37%)

import sys
import inspect
sys.path.insert(0,'..')
from _helper import *
from typing import List


### ADD SOLUTION CLASS HERE 

from collections import Counter
from itertools import combinations
class Solution2:

    def _w2s(self, word):
        return sum(self.score[ch] for ch in word)

    def _chk(self, words):
        l = self.letters.copy()
        for c in "".join(words):
            if not c in l:
                return False
            l.pop(l.index(c))
        return True

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        self.letters = letters
        self.score = {chr(97+i) : _ for i,_ in enumerate(score)}
        self.chart = {word: self._w2s(word) for word in words}
        result = [0,]

        for r in range(len(words)+1):
            for combo in combinations(words, r):
                if self._chk(combo):
                    result.append(sum(self.chart[word] for word in combo))
        return max(result)



class Solution:

    def _w2s(self, word):
        return sum(self.score[ch] for ch in word)

    def _chk(self, words):
        l = self.letters.copy()
        for c in "".join(words):
            if not c in l:
                return False
            l.pop(l.index(c))
        return True

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        self.letters = letters
        self.score = {chr(97+i) : _ for i,_ in enumerate(score)}
        result = [0,]
        for r in range(len(words)+1):
            for combo in combinations(words, r):
                if self._chk(combo):
                    result.append(sum(self._w2s(word) for word in combo))
        return max(result)


if __name__ == "__main__":
    for f in ( 
            ### ADD SOLUTION CLASS LIST HERE 
            Solution(),
            # Solution2(),
            # Solution3(),
            ):
        for e in (
                ### ADD TEST LIST HERE (INPUT, OUTPUT)
                (["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0], 23),

                (["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10], 27),

                (["leetcode"], ["l","e","t","c","o","d"], [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0], 0),

                (["daeagfh","acchggghfg","feggd","fhdch","dbgadcchfg","b","db","fgchfe","baaedddc"], ["a","a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","d","d","d","d","d","d","d","d","d","d","d","d","d","d","e","e","e","e","e","e","e","e","e","e","f","f","f","f","f","f","f","f","f","f","f","f","f","f","g","g","g","g","g","g","g","g","g","g","g","g","h","h","h","h","h","h","h","h","h","h","h","h","h"], [2,1,9,2,10,5,7,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] ,298),


                ):

            # funct = inspect.getmembers(f)[-1][1]
            funct = Solution2()

            print()

            # test_node(funct, e[-1], *e[:-1])

            test(funct.maxScoreWords, e[-1], *e[:-1])
            timer(funct.maxScoreWords, 5, *e[:-1])


            print()
