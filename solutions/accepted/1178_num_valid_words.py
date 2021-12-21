#!/usr/bin/env python3

#1178. Number of Valid Words for Each Puzzle
# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/
# HARD

# Accepted!

# Solution
#https://leetcode.com/submissions/detail/602414269/
# 9343 ms (5.01%)
# 43.7MB (41.84%)

# Solution 2
# https://leetcode.com/submissions/detail/602387004/
# 1493ms
# 42MB


from collections import Counter
class Solution:
    def findNumOfValidWords(self, words=[], puzzle=[]):
        result = [0] * len(puzzle)
        cleanw = Counter(map(frozenset, words))
        firsts = set([_[0] for _ in puzzle])
        cleankey = [_ for _ in cleanw if len(_) < 8 and _ & firsts]
        for pi, puzzle in enumerate(puzzle):
            cleanp = set(puzzle)
            for word in cleankey:
                if puzzle[0] in word and not word.difference(cleanp):
                    result[pi] += cleanw[word]
        return result


# based on topic solution
class Solution2:
    def mask(self, word, mask=0):
        for w in word:
            mask |= 1 << (ord(w) - 97)
        return mask

    def findNumOfValidWords(self, words=[], puzzle=[]):
        result = [0]*len(puzzle)
        cleanw = Counter(map(self.mask, words))
        for pi, puzzle in enumerate(puzzle):
            letter = self.mask(puzzle[0])
            count = cleanw[letter]
            mask = self.mask(puzzle[1:])
            sub = mask
            while sub:
                count += cleanw[sub|letter]
                sub = (sub-1) & mask
            result[pi] += count
        return result


if __name__ == "__main__":

    for ex in (
            (["aaaa","asas","able","ability","actt","actor","access"],
             ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"],
             [1,1,3,2,4,0]
            ),
            (["apple","pleas","please"],
             ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"],
             [0,1,3,2,0]
            ),

            ):

        s = Solution()
        print(s.findNumOfValidWords(ex[0], ex[1]), "--", \
                s.findNumOfValidWords(ex[0], ex[1]) == ex[2])
