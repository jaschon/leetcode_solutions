#!/usr/bin/env python3
# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# Medium

def lenpal(s=""):
    results = []
    longest = 0
    for i1 in range(len(s)+1):
        for i2 in range(i1,len(s)+1):
            sub = s[i1:i2]
            if sub == sub[::-1] and len(sub) > longest:
                longest = len(sub)
                results.append(sub)
    if not results:
        return "" 
    return [i for i in results if len(i) >= longest][0]

if __name__ == "__main__":

    funct = lenpal
    for ex in (
            ("babad", "bab"),
            ("cbbd", "bb"),
            ("a", "a"),
            ("ac", "a"),
            (" ", " "),
            ("", ""),
            ):

        print(ex[0], funct(ex[0]), '--', ex[1] == funct(ex[0]))
