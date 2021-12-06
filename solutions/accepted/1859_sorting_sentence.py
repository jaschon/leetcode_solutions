#!/usr/bin/env python3
# 1859. Sorting the Sentence
# https://leetcode.com/problems/sorting-the-sentence/
# Easy

# Accepted!
# Result: https://leetcode.com/submissions/detail/597861926/
# Time: 24ms (94.80%)
# Mem: 14.2 MB (76.44%)

import sys
sys.path.insert(0,'..')
from _helper import *

class Solution2:
    def sortSentence(self, s: str) -> str:
        return " ".join([_[::-1][:-1] for _ in sorted([_[::-1] for _ in s.split()])])


class Solution:
    def sortSentence(self, s: str) -> str:
        return " ".join([_[::-1][:-1] for _ in sorted([_ for _ in s[::-1].split()])])


if __name__ == "__main__":
    for e in (
            ("is2 sentence4 This1 a3", "This is a sentence"),
            ("Myself2 Me1 I4 and3", "Me Myself and I"),


            ):

        funct = Solution().sortSentence

        print()

        test(funct, e[1], e[0])
        timer(funct, e[0])
        timer(Solution2().sortSentence, e[0])

        print()
