#!/usr/bin/env python3
# https://leetcode.com/problems/count-and-say/
# 38. Count and Say
# Medium
#Accepted!
# https://leetcode.com/problems/count-and-say/submissions/
# 36ms (96.49%)
# 14.5 MB (10.19%)

class Solution:
    def countAndSay(self, n):
        result = "1"
        for i in range(n-1):
            result = self.say(result)
        return result
    
    def say(self, num):
        digits = []
        for n in num:
            if digits and n == digits[-1][0]:
                digits[-1].append(n)
            else:
                digits.append([n,])
        return "".join([f"{len(d)}{d[0]}" for d in digits])

if __name__ == "__main__":
    for ex in (
            (1, "1"),
            (2, "11"),
            (3, "21"),
            (4, "1211"),
            (5, "111221"),
            (6, "312211"),
            (7, "13112221"),
            (8, "1113213211"),
            (9, "31131211131221"),
            (10, "13211311123113112211"),
            ):
        s = Solution()
        print("COUNT", ex[0], s.countAndSay(ex[0]), s.countAndSay(ex[0]) == ex[1])
