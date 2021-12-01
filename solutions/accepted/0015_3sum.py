#!/usr/bin/env python3
# 15. 3Sum
# https://leetcode.com/problems/3sum/
# Accepted 6028ms (8.19%) (SLOOOOW)
# 17.5 MB
 
import timeit

class Solution:
    """2-Pointer"""
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3 : return []
        result = set()
        nums.sort()
        for i in range(len(nums)-2):
            k = i+1
            j = len(nums)-1
            while k < j:
                while nums[i]+nums[j]+nums[k] > 0:
                    if i == j or j==k or i == k:
                        break
                    j -= 1
                while nums[i]+nums[j]+nums[k] < 0:
                    if i == j or j==k or i == k:
                        break
                    k += 1
                if nums[i]+nums[j]+nums[k] == 0 and i != j != k:
                        result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                        k += 1
        return result


class Solution2:
    """TIMED OUT!!!!"""
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        i, j = 0, len(nums)-1
        if j < 1 : return []
        result = set()
        nums = sorted(nums)
        while j > i:
            for k in range(i+1, j):
                if nums[i]+nums[j]+nums[k] == 0:
                    result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    break
            i += 1
            if i == j:
                j -= 1
                i = 0
        return result


class Solution3:
    """TIMED OUT!!!!"""
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        i, j = 0, len(nums)-1
        if j < 1 : return []
        result = set()
        nums = sorted(nums)
        d = {}
        while j > i:
            if not d.get((nums[i], nums[j])):
                add = -1 * (nums[i] +  nums[j])
                d[(nums[i], nums[j])] = add
                if add in nums[i+1:j+1]:
                    k = nums[i+1:j+1].index(add) + i + 1
                    if i != j and j != k and i != k:
                        result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
            i += 1
            if i == j:
                j -= 1
                i = 0
        return result


class Solution4:
    """TIMED OUT!!!!"""
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        i, j = 0, len(nums)-1
        if j < 1 : return []
        result = set()
        nums = sorted(nums)
        d = {}
        while j > i:
            if not d.get((nums[i], nums[j])):
                for k in range(i+1, j):
                    d[(nums[i], nums[j])] = ""
                    if nums[i]+nums[j]+nums[k] == 0:
                        result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                        break
            i += 1
            if i == j:
                j -= 1
                i = 0
        return result
     

if __name__ == "__main__":
    for ex in (
            ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
            ([], []),
            ([0], []),
            ([-1,0,1,2,-1,-4,-2,-3,3,0,4], [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]),
            ([0,0,0], [[0,0,0]]),
            ([0,0,0,0], [[0,0,0]]),
            ([3,2,-2,3,-2,-5,4,-1,-5,4], [[-5,2,3],[-2,-2,4],[-2,-1,3]]),
            ([3,0,-2,-1,1,2], [[-2,-1,3],[-2,0,2],[-1,0,1]]),
            ([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0], [[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]]),
            ):
        result = Solution4().threeSum(ex[0])
        test_len = (len(ex[1]) == len(result))
        test_val = True
        for t in result:
            if not list(t) in ex[1]:
                print("FAIL", t)
                test_val = False
                break
        print(ex[0], "PASS" if test_len and test_val else f"\n--FAIL!--\nRESULT\n{result}\nEXPECTED\n{ex[1]}")

        t1 = timeit.Timer(lambda: Solution().threeSum(ex[0]))
        t2 = timeit.Timer(lambda: Solution2().threeSum(ex[0]))
        t3 = timeit.Timer(lambda: Solution3().threeSum(ex[0]))
        t4 = timeit.Timer(lambda: Solution4().threeSum(ex[0]))
        print("TIMER 1", t1.timeit(5))
        print("TIMER 2", t2.timeit(5))
        print("TIMER 3", t3.timeit(5))
        print("TIMER 4", t4.timeit(5))
        print()


