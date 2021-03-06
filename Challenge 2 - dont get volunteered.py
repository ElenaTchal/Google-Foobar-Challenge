chessboard = [[0, 3, 2, 3, 2, 3, 4, 5],
            [3, 2, 1, 2, 3, 4, 3, 4],
            [2, 1, 4, 3, 2, 5, 4, 5],
            [3, 2, 3, 2, 3, 4, 3, 4],
            [2, 3, 2, 3, 4, 3, 4, 5],
            [3, 4, 5, 4, 3, 4, 5, 4],
            [4, 3, 4, 3, 4, 5, 4, 5],
            [5, 4, 5, 4, 5, 4, 5, 6]]
def num2pos(num):
    return [num / 8, num % 8]
def solution(src, dest):
    [x1, y1] = num2pos(src)
    [x2, y2] = num2pos(dest)
    return chessboard[abs(x1 - x2)][abs(y1 - y2)]

print answer(23, 40)
print answer(19, 36)
print answer(0, 1)
