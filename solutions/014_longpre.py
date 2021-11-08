#!/usr/bin/env python3
# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
# EASY

from collections import Counter

def lcp_b(strs):
    if not strs: return "NONE"
    parts = []
    for s in strs:
        pre = ""
        for ch in s:
            pre += ch
            if len(pre) > 1:
                parts.append(pre)
    return Counter(parts).most_common(1)[0][0] \
            if Counter(parts).most_common(1)[0][1] > 1 else "NONE"

def lcp(strs):
    pre = ""
    if not strs: return "NONE"
    for x, y in zip(strs[0], strs[-1]):
        if x == y:
            pre += x
        else: 
            break
    return pre if pre else "NONE"


if __name__ == "__main__":

    func = lcp_b
    
    for example in (
            (("flower","flow","flight"), "fl"),
            (("dog", "racecar", "car"), "NONE"),
            ((), "NONE"),
            ):

        print(example[0], func(example[0]), "=",  example[1], \
                example[1] == func(example[0])
                )
