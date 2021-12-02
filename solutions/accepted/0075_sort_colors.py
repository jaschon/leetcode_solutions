#!/usr/bin/env python3
# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/
# Medium
# Accepted! (kind of slow)
# https://leetcode.com/submissions/detail/591661454/
# 53ms (7.33%)
# 14mb (99%)

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for j in range(len([_ for _ in nums if _ == 1])+1):
            for i in range(len(nums)):
                if nums[i]== 0:
                    nums.insert(0, nums.pop(i))
                    zeros += 0
                elif nums[i] == 2:
                    nums.append(nums.pop(i))
                else:
                    ones += 1
        return nums

if __name__ == "__main__":
    for ex in (
            ([2,0,2,1,1,0], [0,0,1,1,2,2]),
            ([1,2,0], [0,1,2]),
            ([1,1,2,0], [0,1,1,2]),
            ([2,1,1,2,1,0,2], [0,1,1,1,2,2,2]),
            ([2,1,1,2,1,2], [1,1,1,2,2,2]),
            ([2,2,1], [1,2,2]),
            ([],[]),
            ([1,2,0,0], [0,0,1,2]),
            ([1,2,2,2,2,0,0,0,1,1], [0,0,0,1,1,1,2,2,2,2])

            ):
        result = Solution().sortColors(ex[0])
        # print(ex[0], ex[1], result, "PASS" if result == ex[2] else "FAIL")
        print(ex[0], ex[1], result, "PASS" if result == ex[1] else "FAIL")


