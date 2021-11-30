#!/usr/bin/env python3
# https://leetcode.com/problems/spiral-matrix-ii/
# 59. Spiral Matrix II
# Accepted
# https://leetcode.com/submissions/detail/591676834/
# 52ms
# 14.2 MB

class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        if n == 1: return [[1,],]
        x, y, d, i = 0, 0, 'r', 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        #default direction add 0-1 index. direction change values 2-4 index 
        pos = { 'r' : (1, 0, -1, 1, 'd'),
               'd' : (0, 1, -1, -1, 'l'), 
               'l': (-1, 0, 1, -1, 'u'), 
               'u': (0, -1, 1,1,'r') 
              }
        while matrix[y][x] == 0:
            matrix[y][x] = i 
            x += pos[d][0]
            y += pos[d][1]
            #check for direction change. use index 2-4
            if (x>= n or x<0 or y>=n or y<0 or matrix[y][x] > 0):
                x += pos[d][2]
                y += pos[d][3]
                d = pos[d][4]
            i += 1
        return matrix

if __name__ == "__main__":
    for ex in (
            (3, [[1,2,3],[8,9,4],[7,6,5]]),

            ):
        result = Solution().generateMatrix(ex[0])
        print(ex[0], result, "PASS" if result == ex[1] else "FAIL")


