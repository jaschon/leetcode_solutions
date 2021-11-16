#!/usr/bin/env python3
#https://leetcode.com/problems/length-of-last-word/
# 58. Length of Last Word
# Easy

def lastword(s):
    return len(s.split()[-1])

if __name__ == "__main__":

    funct = lastword
    for ex in (
            ("Hello World", 5),
            ("   fly me   to   the moon  ", 4),
            ("luffy is still joyboy", 6),
            ):

        print(ex[0], funct(ex[0]), ex[1] == funct(ex[0]))

