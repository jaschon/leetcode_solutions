#!/usr/bin/env python3
# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/
# MEDIUM

def convert(s="", rows=1):
    if rows == 1: return s
    x, y, down = 0, 0, True
    s = list(list(zip(*s))[0])
    board = [[" " for _ in range(int((len(s)/2)+.5))] for _ in range(rows)]
    while s:
        board[y][x] = s.pop(0)
        if y == (rows-1):
            down = False
        elif y == 0:
            down = True
        if down:
            y += 1
        else:
            x += 1
            y -= 1
    return "".join(["".join(_) for _ in board]).replace(" ", "")

if __name__ == "__main__":
    funct = convert
    for ex in (
            ("A", 1, "A"), # 1 row, 1 char should match input
            ("PAYPALISHIRING", 1, "PAYPALISHIRING"), # 1 row should match input
            ("PAYPALISHIRING", 14, "PAYPALISHIRING"), # str len should match input
            ("PAYPALISHIRING", 2, "PYAIHRNAPLSIIG"), # 2 row test
            ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"), # 3 row test
            ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"), # 4 row test
            ("PAYPALISHIRING", 5, "PHASIYIRPLIGAN"), # 5 row test
            ("PAYPALISHIRING", 6, "PRAIIYHNPSGAIL"), # 6 row test
            ("PAYPALISHIRING", 7, "PNAIGYRPIAHLSI"), # 7 row test
            ):
        print(ex[0], ex[1], funct(ex[0], ex[1]), ex[2] == funct(ex[0], ex[1]))
