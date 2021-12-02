#!/usr/bin/env python3
# https://leetcode.com/problems/add-binary/
# 67. Add Binary
# Easy
# Accepted
# https://leetcode.com/submissions/detail/589726103/
# 28ms (92.77%)
# 14.4MB

BIN = { 
        "000": "00", 
        "001": "10",
        "010": "10",
        "111": "11", 
        "011": "01", 
        "110": "01", 
        "101": "01", 
        "100": "10", 
        }
class Solution(object):
    def addBinary(self, a, b):
        a, b = a[::-1], b[::-1]
        result = ""
        carry = "0"
        i = 0
        while True:
            n1 = a[i] if i < len(a) else "0"
            n2 = b[i] if i < len(b) else "0"
            # print("ADD", add)
            result = BIN[carry+n1+n2][0] + result
            carry = BIN[carry+n1+n2][1]
            i += 1
            if i >= len(a) and i >= len(b):
                if carry == "1": result = "1" + result
                break
            # print("result", result, "carry", carry)
        # print("end", result)
        return result


            


if __name__ == "__main__":
    funct = Solution().addBinary
    for ex in (
            ("11", "1", "100"),
            ("1010", "1011", "10101"),
            ("10001", "11101","101110"),
            ("000", "000", "000")
            ):
        result = funct(ex[0], ex[1])
        print(ex[0], "+", ex[1], "=", result, "PASS" if result == ex[-1] else "FAIL")


