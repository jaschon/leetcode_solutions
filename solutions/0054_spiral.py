#!/usr/bin/env python3
# https://leetcode.com/problems/spiral-matrix/
# 54. Spiral Matrix
# Medium

def spiral(matrix):
    result = []
    x, y, d = 0, 0, 'r'
    w, h = len(matrix[0]), len(matrix)
    direction = { 'r' : (1, 0), 'd' : (0, 1), 'l': (-1, 0), 'u': (0, -1) }
    while matrix[y][x]:
        result.append(matrix[y][x])
        matrix[y][x] = ""
        x += direction[d][0]
        y += direction[d][1]
        if (x < w and d == 'r' and not matrix[y][x]) or x == w:
            x -= 1
            y += 1
            d = 'd'
        elif (y < h and d == 'd' and not matrix[y][x]) or y == h:
            y -= 1
            x -= 1
            d = 'l'
        elif (x > -1 and d == 'l' and not matrix[y][x]) or x == -1:
            x += 1
            y -= 1
            d = 'u'
        elif d == 'u' and not matrix[y][x]:
            y += 1
            x += 1
            d = 'r'
    return result

if __name__ == "__main__":
    funct = spiral
    for ex in (
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
        result = funct(ex[0])
        print(example, result, result == ex[1])

