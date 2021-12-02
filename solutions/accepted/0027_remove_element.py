#!/usr/bin/env python3
# https://leetcode.com/problems/remove-element/
# 27. Remove Element
# Easy
# Accepted!
# https://leetcode.com/problems/remove-element/submissions/
# 56ms (8.89%)
# 14.3MB (15.34%)

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.pop(nums.index(val))
        return len(nums)



if __name__ == "__main__":
    for ex in (
            ([3,2,2,3], 3, 2, [2,2]),
            ([0,1,2,2,3,0,4,2], 2, 5, [0,1,3,0,4])
            ):
        num = Solution().removeElement(ex[0], ex[1])
        print(num, ex[0], "PASS" if ex[0] == ex[3] and num == ex[2] else "FAIL")


