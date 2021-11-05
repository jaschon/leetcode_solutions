#!/usr/bin/env python3
# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
# EASY

from collections import deque

ROM = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
        }

FIX = {
        'I' : 'VX',
        'X' : 'LC',
        'C' : 'DM',
        }


def rom2int(s=""):
    digits = deque(list(zip(*s))[0])
    total = 0
    while digits:
        d1 = digits.popleft()
        if digits and d1 in FIX:
            d2 = digits.popleft()
            if d2 in FIX.get(d1,""):
                total += (ROM.get(d2, 0) - ROM.get(d1, 0))
            else:
                total += ROM.get(d1, 0)
                digits.appendleft(d2)
        else:
            total += ROM.get(d1, 0)
    return total



if __name__ == "__main__":

    for example in (
            ("I", 1),
            ("V", 5),
            ("X", 10),
            ("III", 3),
            ("IIII", 4),
            ("IV", 4),
            ("IX", 9),
            ("LVIII", 58),
            ("MCMXCIV", 1994),
            ("XXXIX", 39),
            ("CCXLVI", 246),
            ("CLX", 160),
            ("DCCLXXXIX", 789),
            ("MMCDXXI", 2421),
            ("MIX", 1009),
            ("MLXVI", 1066),
            ("MDCCLXXVI", 1776),
            ("MCMXVIII", 1918),
            ("MCMLIV", 1954),
            ("MMXIV", 2014),
            ("MMMCMXCIX", 3999),
            ("this should fail!", 0),
            ):

        print(example[0], "::", \
                rom2int(example[0]), "=", example[1], \
                rom2int(example[0]) == example[1]
                )









