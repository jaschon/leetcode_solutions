#!/usr/bin/env python3
# https://leetcode.com/problems/count-and-say/
# 38. Count and Say
# Medium

def say(num):
    digits = []
    for n in num:
        if digits and n == digits[-1][0]:
            digits[-1].append(n)
        else:
            digits.append([n,])
    return "".join([f"{len(d)}{d[0]}" for d in digits])

def count_say(n):
    result = "1"
    for i in range(n-1):
        result = say(result)
    return result

if __name__ == "__main__":
    funct = count_say
    print("SAY", "3322251", say("3322251"), say("3322251") == "23321511")
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
        print("COUNT", ex[0], funct(ex[0]), funct(ex[0]) == ex[1])
