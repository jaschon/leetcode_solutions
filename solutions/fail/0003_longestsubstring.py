#!/usr/bin/env python3
# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Medium

# FAIL! Time Limit!!!

from collections import Counter

def lensub(s=""):
    results = []
    longest = 0
    for i1 in range(len(s)+1):
        for i2 in range(i1,len(s)+1):
            sub = ''.join(set(s[i1:i2]))
            if sub and len(sub) == len(s[i1:i2]) and len(sub) > longest:
                longest = len(sub)
                results.append(s[i1:i2])
    if not results:
        return 0
    return len(Counter([i for i in results if len(i) >= longest]).most_common(1)[0][0])

if __name__ == "__main__":

    funct = lensub
    for ex in (
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("pwwkew", 3),
            ("", 0),
            ):

        print(ex[0], funct(ex[0]), '--', ex[1] == funct(ex[0]))
