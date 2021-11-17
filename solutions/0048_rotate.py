#!/usr/bin/env python3
# https://leetcode.com/problems/rotate-image/
# 48. Rotate Image
# Medium

#slow and dirty. concat new numbers to old and strip off excess before returning
def rotate_dirty(matrix):
    w = len(matrix[0]) - 1
    h = len(matrix) - 1
    for r, row in enumerate(matrix):
        for c, col in enumerate(matrix[r]):
            matrix[c][w-r] = f"{matrix[r][c]} {matrix[c][w-r]}"
    for r in range(h+1):
        for c in range(w+1):
            if r == 0:
                matrix[r][c] = int(matrix[r][c].split()[0])
            else:
                matrix[r][c] = int(matrix[r][c].split()[-2])
    return matrix

# swap the numbers in a "diamond" shape. 
def rotate(matrix):
    l = len(matrix[0]) - 1 #h should be same as w.
    for col in range(int(len(matrix)/2) + (len(matrix) % 2)): #need an extra loop if not div 2
        for row in range(int(len(matrix)/2)):

            tmp = matrix[row][col] #store 1st pos, so you don't wack it

            # MOVE 4th to 1st Pos
            # print(matrix[l-col][row-l-1], "to", matrix[row][col])
            matrix[row][col] = matrix[l-col][row-l-1]

            # MOVE 3rd to 4th Pos
            # print(matrix[l-row][l-col], "to", matrix[l-col][row-l-1])
            matrix[l-col][row-l-1] = matrix[l-row][l-col]

            # MOVE 2nd to 3rd Pos
            # print(matrix[col][w-row], "to", matrix[l-row][w-col])
            matrix[l-row][l-col] = matrix[col][l-row]

            #MOVE 1st (TMP) to 2nd Pos
            # print(tmp, "to", matrix[col][l-row])
            matrix[col][l-row] = tmp

            # print()
    # print(matrix)
    return matrix

if __name__ == "__main__":
    funct = rotate
    for ex in (
            ([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]),
            ([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]], [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]),
            ([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20], [21,22,23,24,25]], \
                    [[21,16,11,6,1], [22,17,12,7,2], [23,18,13,8,3], [24,19,14,9,4], [25,20,15,10,5]]),
            ):
        result = funct(ex[0])
        print(ex[1], ex[1] == result)
