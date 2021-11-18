#!/usr/bin/env python3

#1178. Number of Valid Words for Each Puzzle
# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/
# HARD
# FAIL! TIME OUT!

class Solution:
    def findNumOfValidWords(self, words=[], puzzle=[]):
        result = [0 for _ in range(len(puzzle))]
        cleanp = ["".join(sorted(set(_)))+str(i) for i,_ in enumerate(puzzle)]
        cleanw = ["".join(sorted(set(_))) for _ in words]
        for word in cleanw:
            check = cleanp.copy()
            for ch in word:
                check = [_ for _ in check \
                        if ch in _ and puzzle[cleanp.index(_)][0] in word]
                if not check: break
                if ch == word[-1]:
                    for success in check:
                        result[cleanp.index(success)] += 1
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
