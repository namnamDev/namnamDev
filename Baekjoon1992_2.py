import sys
from collections import deque

sys.stdin = open("Baekjoon1992.txt")


def quad(start, end):
    print(end)
    Q.append("(")
    if start == end:
        Q.append(board[start][start])
    else:
        temp = board[start[0]][start[1]]
        print(start, start, temp)
        for i in range(start[0], end[0] // 2):
            for g in range(start[1], end[1] // 2):
                if temp != board[i][g]:
                    quad(start, [end[0] // 2, end[0] // 2])
                    break

        Q.append(temp)
        Q.append(")")

        temp2 = board[start[0]][end[0] // 2]
        print(0, end // 2, temp2)
        for i in range(start, end // 2):
            for g in range(end // 2, end):
                if temp2 != board[i][g]:
                    quad(board, end // 2)
                    break
        Q.append(temp2)
        Q.append(")")

        temp3 = board[end // 2][start]
        print(end // 2, 0, temp3)
        for i in range(end // 2, end):
            for g in range(start, end // 2):
                if temp3 != board[i][g]:
                    quad(board, end // 2)
                    break

        Q.append(temp3)
        Q.append(")")
        temp4 = board[end // 2][end // 2]
        print(end // 2, end // 2, temp4)
        for i in range(end // 2, end):
            for g in range(end // 2, end):
                if temp4 != board[i][g]:
                    quad(board, end // 2)
                    break
        Q.append(temp4)
        Q.append(")")


T = int(input())
board = [list(map(int, input())) for _ in range(T)]
for i in board:
    print(i)
Q = []
quad([0, 0], [T, T])

print(*Q)
