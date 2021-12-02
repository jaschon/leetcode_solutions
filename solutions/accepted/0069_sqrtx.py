#!/usr/bin/env python3
# https://leetcode.com/problems/sqrtx/
# 69. Sqrt(x)
# Easy
# Accepted
# https://leetcode.com/submissions/detail/591684806/
# 37ms (60.84%)
# 14.3MB (41.63)

class Solution:
    def mySqrt(self, n: int) -> int:
        # Babylonian Method?
        x = n
        y = 1
        while(x > y):
            x = (x+y)//2
            y = n//x
        return x


if __name__ == "__main__":
    for ex in (
            (4, 2),
            (8, 2),
            ):
        result = Solution().mySqrt(ex[0])
        print(ex[0], result, "PASS" if result == ex[1] else "FAIL")


