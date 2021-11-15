#!/usr/bin/env python3
# https://leetcode.com/problems/valid-sudoku/
# 36. Valid Sudoku
# Medium

class CheckSudoku:

    def __init__(self, board=[]):
        self.board = board

    def check(self):
        return all((self.check_rows(), self.check_cols(), self.check_boxes()))

    def is_valid(self, arr):
        cmp = [0 for _ in range(0, 10) ]
        for num in arr:
            if num.isdigit():
                if cmp[int(num) - 1] > 0:
                    return False
                cmp[int(num)-1] += 1
        return sum(cmp) < 10 

    def valid_col(self, row):
        tmp = [self.board[col][row] for col in range(0, 9) ]
        return self.is_valid(tmp)

    def valid_row(self, col):
        return self.is_valid(self.board[col])

    def valid_box(self, col, row):
        tmp = []
        tmp = self.board[col][row: row+3] + \
                self.board[col+1][row: row+3] + \
                self.board[col+2][row: row+3]
        return self.is_valid(tmp)

    def check_rows(self):
        for col in range(0, 9):
            if not self.valid_row(col):
                return False
        return True

    def check_cols(self):
        for row in range(0, 9):
            if not self.valid_col(row):
                return False
        return True

    def check_boxes(self):
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if not self.valid_box(col, row):
                    return False
        return True

if __name__ == "__main__":

    for ex in (
        ([
         ["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]
        ], True),

        ([
         ["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]
        ], False),
        ):
            c = CheckSudoku(ex[0])
            print("check rows", c.check_rows())
            print("check cols", c.check_cols())
            print("check boxes", c.check_boxes())
            print("is valid?", c.check())
            print("pass test?", ex[1] == c.check())
            print()

