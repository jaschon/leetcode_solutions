#!/usr/bin/env python3
#66. Plus One
# https://leetcode.com/problems/plus-one/
# EASY
# Accepted!
# https://leetcode.com/submissions/detail/589199268/
# 32ms (71.89%)
# 14.4MB (15.03%)

class Solution:
    def plusOne(self, s=[]):
        return [int(i) for i in str(int(''.join([str(x) for x in s]))+1)]


if __name__ == "__main__":
    for example in (
            ([1,2,3], [1,2,4]),
            ([4,3,2,1], [4,3,2,2]),
            ([0], [1]),
            ([9], [1,0]),
            ):
        s = Solution()
        print(example[0], \
                s.plusOne(example[0]), "=", example[1], \
                s.plusOne(example[0]) == example[1],
                )
