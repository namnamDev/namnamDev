import sys

sys.stdin = open("Baekjoon2324.txt")

from collections import deque


def check(paArr):
    aa = paArr[0][0]
    for y in range(m):
        for x in range(n):
            if paArr[y][x] != aa:
                return False
    return True


def copyArr(paArr):
    tempArr = [[0] * n for _ in range(m)]
    for y in range(m):
        for x in range(n):
            tempArr[y][x] = paArr[y][x]
    return tempArr


diry = [0, 0, -1, 1]
dirx = [-1, 1, 0, 0]
n, m = map(int, input().split())
board = []
for _ in range(m):
    board.append(list(map(int, input())))
for i in board:
    print(i)
