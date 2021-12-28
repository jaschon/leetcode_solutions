#!/usr/bin/env python3
# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/
# MEDIUM
# Accepted!
# https://leetcode.com/submissions/detail/608176648/
# 452ms, 18.1mb

class Solution:
    def convert(self, s="", rows=1):
        if len(s) == 1 or rows == 1: return s
        x, y, down = 0, 0, True
        board = [["" for _ in range(int((len(s)/2)+.5))] for _ in range(rows)]
        for char in s:
            board[y][x] = char
            if y == (rows-1):
                down = False
            elif y == 0:
                down = True
            if down:
                y += 1
            else:
                x += 1
                y -= 1
        return "".join(["".join(_) for _ in board if _])

if __name__ == "__main__":
    for ex in (
            ("ABC", 2, "ACB"),
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
        s = Solution()
        print(ex[0], ex[1], s.convert(ex[0], ex[1]), ex[2] == s.convert(ex[0], ex[1]))
