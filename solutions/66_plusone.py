#!/usr/bin/env python3
#66. Plus One
# https://leetcode.com/problems/plus-one/
# EASY

def plus_one(s=[]):
    return [int(i) for i in str(int(''.join([str(x) for x in s]))+1)]


if __name__ == "__main__":
    funct = plus_one
    for example in (
            ([1,2,3], [1,2,4]),
            ([4,3,2,1], [4,3,2,2]),
            ([0], [1]),
            ([9], [1,0]),
            ):

        print(example[0], \
                funct(example[0]), "=", example[1], \
                funct(example[0]) == example[1],
                )
