#!/usr/bin/env python3
#273. Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/
# HARD
# Accepted!
# https://leetcode.com/submissions/detail/589185562/
# 28ms (92.17%!!)
# 14.5MB (26.54%)

ONES = ("", "One", "Two", "Three", "Four", "Five", \
        "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
        "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty")
TENS = ("", "Ten", "Twenty", "Thirty", "Forty", "Fifty", \
        "Sixty", "Seventy", "Eighty", "Ninety", "Hundred")
HUNDREDS = ("", "Hundred", "Thousand", "Million", "Billion", "Trillion", 
        "Quadrillion", "Quintillion")

class Solution:
    def numberToWords(self, s=""):
        s = str(s)[::-1]
        digits = [s[i:i + 3][::-1] for i in range(0, len(s), 3)][::-1]
        result = []
        for i, d in enumerate(digits):
            if d == "000": continue
            if d == "0":
                result.append("Zero")
                continue
            if int(d) > 99:
                result.append(ONES[int(d[0])])
                result.append(HUNDREDS[1])
                d = d[1:]
            if int(d) < 21:
                result.append(ONES[int(d)])
            else:
                d = d.lstrip("0")
                result.append(TENS[int(d[0])])
                result.append(ONES[int(d[1])])
            if len(digits) > 1 and i != (len(digits)-1):
                result.append(HUNDREDS[len(digits)-i])
        return " ".join([_ for _ in result if _])

if __name__ == "__main__":
    for ex in (
            (1099, "One Thousand Ninety Nine"), #the one I missed. :(
            (0, "Zero"),
            (1, "One"),
            (4, "Four"),
            (10, "Ten"),
            (14, "Fourteen"),
            (24, "Twenty Four"),
            (123, "One Hundred Twenty Three"),
            (12345, "Twelve Thousand Three Hundred Forty Five"),
            (120345, "One Hundred Twenty Thousand Three Hundred Forty Five"),
            (1234567, "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"),
            (1234567891, "One Billion Two Hundred Thirty Four Million "
                "Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"),
            (1_001, "One Thousand One"),
            (100_000, "One Hundred Thousand"),
            (100_001, "One Hundred Thousand One"),
            (100_011, "One Hundred Thousand Eleven"),
            (100_100, "One Hundred Thousand One Hundred"),
            (101_010, "One Hundred One Thousand Ten"),
            (1_000_000_001, "One Billion One"),
            (10_000_000_001, "Ten Billion One"),
            (100000000001, "One Hundred Billion One"),
            (1000000000001, "One Trillion One"),
            (10_000_100_000_001, "Ten Trillion One Hundred Million One"),
            (999_000_900_000_011, "Nine Hundred Ninety Nine Trillion Nine Hundred Million Eleven"),
            (99_999_000_900_000_011, "Ninety Nine Quadrillion Nine Hundred Ninety Nine Trillion "
                "Nine Hundred Million Eleven"),
            (112_112_112_112_112_112, "One Hundred Twelve Quadrillion "
                "One Hundred Twelve Trillion One Hundred Twelve Billion "
                "One Hundred Twelve Million One Hundred Twelve Thousand One Hundred Twelve"),
            ):
        s = Solution()
        print(ex[0], s.numberToWords(ex[0]), "--", ex[1] == s.numberToWords(ex[0]))
