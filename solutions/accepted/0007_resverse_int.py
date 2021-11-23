#!/usr/bin/env python3
# https://leetcode.com/problems/reverse-integer/
# 7. Reverse Integer
# Medium
# Accepted!
# https://leetcode.com/problems/reverse-integer/submissions/
# 26ms (90.23%)
# 14.3MB (46.51)

class Solution:
    def reverse(self, x: int) -> int:
        if -2147483649 < x > 2147483648: return 0
        r = int(str(abs(x))[::-1])
        if -2147483649 < r > 2147483648: return 0
        if x < 0: r = r*-1
        return r


if __name__ == "__main__":
    for ex in (
            (123, 321),
            (-123, -321),
            (1534236469, 0),
            ):
        result = Solution().reverse(ex[0])
        print(ex[0], result, "PASS" if result == ex[1] else "FAIL")


