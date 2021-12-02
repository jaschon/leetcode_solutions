#!/usr/bin/env python3
# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/
# Easy

# Accepted! Solution2
# https://leetcode.com/submissions/detail/595966180/
# 32ms (67.29%)
# 14.4 MB (25.10%)

# Accepted! Solution 1
# https://leetcode.com/submissions/detail/595967777/
# 28ms (87.28%)
# 14.4MB (25.10%)


import timeit

class Solution2:
    def generate(self, n: int) -> list[list[int]]:
        result = []
        for line in range(1, n + 1):
            count = 1;
            row = []
            for i in range(1, line + 1):
                row.append(count)
                count = int(count * (line - i) / i);
            result.append(row)
        return result


class Solution:
    def generate(self, n: int) -> list[list[int]]:
        result = []
        for line in range(1, n + 1):
            count = 1;
            result.append([])
            for i in range(1, line + 1):
                result[line-1].append(count)
                count = int(count * (line - i) / i);
        return result

if __name__ == "__main__":
    for ex in (
            (5, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),

            ):
        result = Solution().generate(ex[0])
        t = timeit.Timer(lambda: Solution().generate(ex[0]))
        t2 = timeit.Timer(lambda: Solution2().generate(ex[0]))

        print(ex[0], result, "PASS" if result == ex[1] else "FAIL")
        print("TIMER", t.timeit(5))
        print("TIMER", t2.timeit(5))


