#!/usr/bin/env python3
# https://leetcode.com/problems/ransom-note/
# 383. Ransom Note
# Easy

# Accepted
# Result: https://leetcode.com/submissions/detail/599043926/
# Time: 48ms (82.76%)
# Mem: 14.3MB (64.49)

import sys
sys.path.insert(0,'..')
from _helper import *

class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = False
        magazine = list(list(zip(*magazine))[0])
        for ch in ransomNote:
            if not ch in magazine:
                return False
            else:
                magazine.pop(magazine.index(ch))
        return True

class Solution3:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = False
        mapper = {}
        for ch in magazine:
            mapper[ch] = mapper.get(ch,0)+1
        for ch in ransomNote:
            if not mapper.get(ch) or mapper.get(ch) == 0:
                return False
            else:
                mapper[ch] -= 1
        return True
      
class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mapper = Counter(magazine)
        for ch in ransomNote:
            if not ch in mapper or mapper[ch] == 0:
                return False
            else:
                mapper[ch] -= 1
        return True


from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mapper = Counter(magazine)
        note = Counter(ransomNote)
        for ch in note:
            if not ch in mapper or mapper[ch] < note[ch]:
                return False
        return True


if __name__ == "__main__":
    for e in (

            ("a", "b", False),
            ("aa", "ab", False),
            ("aa", "aab", True),
            ("aab", "baa", True),


            ):

        funct = Solution().canConstruct

        print()

        test(funct, e[2], e[0], e[1])

        print()

        print("FASTEST")
        timer(funct, e[0], e[1])
        print()

        print("Collection")
        timer(Solution1().canConstruct, e[0], e[1])
        print()

        print("Dict")
        timer(Solution2().canConstruct, e[0], e[1])
        print()

        print("Zip")
        timer(Solution3().canConstruct, e[0], e[1])
        print()

        print()
