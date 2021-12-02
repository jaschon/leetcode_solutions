#!/usr/bin/env python3
# 415. Add Strings
# Easy
# https://leetcode.com/problems/add-strings/
# Accepted
# https://leetcode.com/submissions/detail/591160939/
# 44ms (64.32)
# 14.2MB (95.67%)

class Solution(object):
    def addStrings(self, num1, num2):
        i = 1
        carry = 0
        total = ""
        while True:
            n1 = num1[0-i] if len(num1) >= i else 0
            n2 = num2[0-i] if len(num2) >= i else 0
            add = (int(n1)+int(n2)+carry)
            carry = add // 10
            total = f"{add % 10}{total}"
            i += 1
            if i > len(num1) and i > len(num2): break
        if carry: total = f"{carry}{total}"
        return total



if __name__ == "__main__":
    for ex in (
            ("11", "123", "134"),

            ):
        result = Solution().addStrings(ex[0], ex[1])
        print(ex[0], ex[1], result, "PASS" if result == ex[2] else "FAIL")


