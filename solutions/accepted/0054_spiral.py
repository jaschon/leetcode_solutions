#!/usr/bin/env python3
# https://leetcode.com/problems/spiral-matrix/
# 54. Spiral Matrix
# Medium
# Accepted!
# https://leetcode.com/submissions/detail/589203686/
# 32ms (63.53%)
# 14.2MB (59.81%)

class Solution:
    def spiralOrder(self, matrix):
        result = []
        x, y, d = 0, 0, 'r'
        w, h = len(matrix[0]), len(matrix)
        if h == 1: return matrix[0]
        #default direction add 0-1 index. direction change values 2-4 index 
        pos = { 'r' : (1, 0, -1, 1, 'd'),
               'd' : (0, 1, -1, -1, 'l'), 
               'l': (-1, 0, 1, -1, 'u'), 
               'u': (0, -1, 1,1,'r') 
              }
        while matrix[y][x] != "-":
            result.append(matrix[y][x])
            matrix[y][x] = "-"
            x += pos[d][0]
            y += pos[d][1]
            #check for direction change. use index 2-4
            if (x>= w or x<0 or y>=h or y<0 or matrix[y][x] == "-"):
                x += pos[d][2]
                y += pos[d][3]
                d = pos[d][4]
        return result

if __name__ == "__main__":
    for ex in (
            ([[1]], [1]),
            ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]),
            ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]),
            ([[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16]], \
                    [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]),
            ([[1,2,3,4],[5,6,7,8],[9,10,11,12], [13,14,15,16], [17, 18, 19, 20]], \
                    [1,2,3,4,8,12,16,20,19,18,17,13,9,5,6,7,11,15,14,10]),
            ([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]], \
                    [1,2,3,6,9,12,15,14,13,10,7,4,5,8,11]),
            ):
        example = ex[0].copy()
        result = Solution().spiralOrder(ex[0])
        print(example, result, result == ex[1])

