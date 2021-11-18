#!/usr/bin/env python
# https://leetcode.com/problems/search-insert-position/
# 35. Search Insert Position
# Easy
# Accepted!
# https://leetcode.com/submissions/detail/589222898/
# 44ms (91.80%)
# 15.1MB (56.50%)

class Solution:
    def searchInsert(self, nums, target):
        for n in range(len(nums)):
            if n == 0 and target < nums[n]:
                return 0
            elif nums[n] == target:
                return n
            elif target < nums[n]:
                return n
            elif nums[-1] == nums[n]:
                return n+1


if __name__ == "__main__":
    for ex in (
            ([1,3,5,6], 5, 2),
            ([1,3,5,6], 2, 1),
            ([1,3,5,6], 7, 4),
            ([1,3,5,6], 0, 0),
            ([1], 0, 0),
            ):
        result = Solution().searchInsert(ex[0], ex[1])
        print(ex[0], result, result == ex[2])
