#!/usr/bin/env python3
#21. Merge Two Sorted Lists
# EASY
# https://leetcode.com/problems/merge-two-sorted-lists/


#WRONG! USE linked lists, not python lists!!!!!!!

from collections import deque

def m2l(l1, l2):
    l1, l2, merged = deque(l1), deque(l2), []
    itm1, itm2 = "", ""
    while l1 or l2:
        if itm1 == "" and l1:
            itm1 = l1.popleft()
        if itm2 =="" and l2:
            itm2 = l2.popleft()
        if itm1 != "" and itm2 != "":
            if itm1 == itm2:
                merged.append(itm1)
                merged.append(itm2)
                itm2 = ""
                itm1 = ""
            elif itm1 < itm2:
                merged.append(itm1)
                itm1 = ""
            elif itm2 < itm1:
                merged.append(itm2)
                itm2 = ""
        elif itm1:
            merged.append(itm1)
            itm1 = ""
        elif itm2:
            merged.append(itm2)
            itm2 = ""
        else:
            break
    if itm1 != "" and not l1:
        merged.append(itm1)
    elif itm2 != "" and not l2:
        merged.append(itm2)

    return merged 

if __name__ == "__main__":
    funct = m2l
    for example in (
            ([0,1,2,4], [1,3,4], [0,1,1,2,3,4,4]),
            ([1,2,4,5,6,8,21], [9, 13, 22], [1,2,4,5,6,8,9,13,21,22]),
            ([1,2,4,5,6,8,21,23,50], [9, 13, 22], [1,2,4,5,6,8,9,13,21,22,23,50]),






            ):

        print(example[0], example[1], \
                funct(example[0], example[1]), "=", example[2], \
                funct(example[0], example[1]) == example[2],
                )
