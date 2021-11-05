#!/usr/bin/env python3
#273. Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/
# HARD

ONES = ("", "One", "Two", "Three", "Four", "Five", \
        "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
        "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty")
TENS = ("", "Ten", "Twenty", "Thirty", "Forty", "Fifthy", \
        "Sixty", "Seventy", "Eighty", "Ninety", "Hundred")
HUNDREDS = ("", "Hundred", "Thousand", "Million", "Billion", "Trillion", "Quadrillion")

def int2english(s=""):
    s = str(s)[::-1]
    digits = [s[i:i + 3][::-1] for i in range(0, len(s), 3)][::-1]
    result = []
    for i, d in enumerate(digits):
        if d == "0":
            result.append("Zero")
        elif int(d) > 99:
            result.append(ONES[int(d[0])])
            result.append(HUNDREDS[1])
            result.append(TENS[int(d[1])])
            result.append(ONES[int(d[2])])
        elif int(d) > 21:
            result.append(TENS[int(d[0])])
            result.append(ONES[int(d[1])])
        else:
            result.append(ONES[int(d)])
        if d != digits[-1] and len(digits) > 1:
            result.append(HUNDREDS[len(digits)-i])
    return " ".join(result).replace("  "," ")


if __name__ == "__main__":
    funct = int2english
    for ex in (
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
            ):

        print(ex[0], funct(ex[0]), "--", \
                ex[1] == funct(ex[0])
            )

