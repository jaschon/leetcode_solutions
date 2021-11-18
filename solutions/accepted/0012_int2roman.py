#!/usr/bin/env python3
#12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/
#MEDIUM
# Accepted!
# https://leetcode.com/submissions/detail/589163970/
# 28ms (99.94% faster than all py3 subs!)
# 14.1 MB

class Solution:
    def intToRoman(self, s=""):
        roman = "IXCMVLD" #I, X, C, M are in index pos. Add +1 to pos to get special 5's cases
        digits = str(s)[::-1] #to lowest to highest
        result = ""
        if digits and len(digits) < 5 and int(s) > 0 and int(s) < 4000: #check if s > 0 and s < 4000
            for i, d in enumerate(digits):
                d = int(d)
                if d == 9: #9's case (IV, IX...)
                    result = (roman[i] + roman[i+1]) + result
                elif d > 5: #add after 5's case (VI, VII, VIII...)
                    result = (roman[4+i] + (roman[i] * (d-5))) + result
                elif d > 3: #4 and 5's case (IV, V)
                    result = ((roman[i] * (5-d)) + roman[4+i]) + result
                else: #else add amount (I, II, III...)
                    result = (roman[i] * d) + result
        return result

if __name__ == "__main__":
    for ex in (
            (0, ""),
            (1, "I"),
            ('2', "II"),
            (3, "III"),
            (4, "IV"),
            (9, "IX"),
            (58, "LVIII"),
            (160, "CLX"),
            (246, "CCXLVI"),
            (1776, "MDCCLXXVI"),
            (1066, "MLXVI"),
            (1994, "MCMXCIV"),
            (1918, "MCMXVIII"),
            (3999, "MMMCMXCIX"),
            (99999, ""),
            ("this should fail", ""),
            ):

        s = Solution()
        print(ex[0], s.intToRoman(ex[0]), ex[1] == s.intToRoman(ex[0]))
