#!/usr/bin/env python3
# 2062. Count Vowel Substrings of a String
# https://leetcode.com/problems/count-vowel-substrings-of-a-string/
# Easy

# Accepted (solution old)
# Result: https://leetcode.com/submissions/detail/598431958/
# Time: 808ms (12.34%)
# Mem: 14.3MB (21.20%)

# Accepted (solution new)
# Result: https://leetcode.com/submissions/detail/598484977/
# Time: 487ms (19.82%)
# Mem: 14.4MB (21.18%)

# Accepted (solution)
# Result: https://leetcode.com/submissions/detail/598445217/
# Time: 203ms (42.11%)
# Mem: 14.2MB (53.89%)

import sys
sys.path.insert(0,'..')
from _helper import *

import itertools as it

vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
vset = set(('a','e','i','o','u'))

class Solution:
    def test(self, sub):
        subset = set(sub)
        return subset == vset and len(subset) == 5

    def countVowelSubstrings(self, word: str) -> int:
        i, result = 0, 0
        end = len(word) -1
        if end < 4: return result
        while end > 3:
            if word[end] in vowels:
                break
            end -= 1
        for i in range(len(word)):
            j = end
            if not word[i] in vowels:
                continue
            while j-i > 3:
                if word[j] in vowels and self.test(word[i:j+1]):
                    result += 1
                j -= 1
        return result

class SolutionORIG:
    def test(self, sub):
        cmp = [0,0,0,0,0]
        for c in sub:
            if not c in vowels:
                return False
            else:
                cmp[vowels[c]] = 1
        return sum(cmp) == 5

    def countVowelSubstrings(self, word: str) -> int:
        i, result = 0, 0
        end = len(word) -1
        if end < 4: return result
        while end > 3:
            if word[end] in vowels:
                break
            end -= 1
        for i in range(len(word)):
            j = end
            if not word[i] in vowels:
                continue
            while j-i > 3:
                if word[j] in vowels and self.test(word[i:j+1]):
                    result += 1
                j -= 1
        return result


def window(iter, size):
    return zip(*[it.islice(iter, s, None) for s in reversed(range(size))])

class SolutionNEW:
    def countVowelSubstrings(self, word: str) -> int:
        result = 0
        end = 5
        length = len(word)
        while end <= length:
            for w in window(word, end):
                if set(w) == vset:
                    result += 1
            end += 1
        return result

if __name__ == "__main__":
    for e in (

            ("aeiouu", 2),
            ("unicornarihan", 0),
            ("cuaieuouac", 7),
            ("bbaeixoubb", 0),
            ("", 0),
            ):

        funct = Solution().countVowelSubstrings
        funct2 = SolutionNEW().countVowelSubstrings
        funct3 = SolutionORIG().countVowelSubstrings

        print()

        print("SUBMITTED")
        test(funct, e[1], e[0])
        timer(funct, e[0])

        print()

        print("NEW ONE")
        test(funct2, e[1], e[0])
        timer(funct2, e[0])

        print()

        print("ORIG")
        test(funct3, e[1], e[0])
        timer(funct3, e[0])

        print()
