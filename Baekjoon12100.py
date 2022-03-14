import sys

sys.stdin = open('Baekjoon12100.txt')
from collections import deque


def copy(pa):
    t = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            t[y][x] = pa[y][x]
    return t


def to_up(pa):
    for x in range(N):
        for y in range(0, N - 1, 2):
            print(y, x)
            if pa[y][x] == pa[y + 1][x]:
                pa[y][x] *= 2
                pa[y + 1][x] = 0
        for yy in range(N - 1):
            while not pa[yy][x]:
                for yyy in range(yy + 1, N):
                    if pa[yyy][x]:
                        pa[yy][x], pa[yyy][x] = pa[yyy][x], pa[yy][x]
                        break
    return pa


def to_left(pa):
    for y in range(N):
        for x in range(0, N - 1, 2):
            if pa[y][x] == pa[y][x + 1]:
                pa[y][x] *= 2
                pa[y][x + 1] = 0
        print("be")
        for i in pa:
            print(i)
        for xx in range(N - 1):
            while not pa[y][xx]:
                for xxx in range(xx + 1, N):
                    if pa[y][xxx]:
                        pa[y][xxx], pa[y][xx] = pa[y][xx], pa[y][xxx]
                        break
        print("af")
        for i in pa:
            print(i)
    return pa


def to_down(pa):
    for x in range(N):
        for y in range(N - 2, -1, -2):
            if pa[y][x] == pa[y - 1][x]:
                pa[y + 1][x] *= 2
                pa[y][x] = 0

        for yy in range(N - 1, 0, -1):
            while not pa[yy][x]:
                for yyy in range(N - yy - 1, -1, -1):
                    if pa[yyy][x]:
                        pa[yy][x], pa[yyy][x] = pa[yyy][x], pa[yy][x]
                        break
    return pa


def to_right(pa):
    for y in range(N):
        for x in range(N - 1, -1, -2):
            print(y, x, pa[y][x], pa[y][x - 1])
            if pa[y][x] == pa[y][x - 1]:
                pa[y][x] *= 2
                pa[y][x - 1] = 0
        for i in pa:
            print(i)
        for xx in range(N - 1, 0, -1):
            if not pa[y][xx]:
                for xxx in range(N - xx - 1, -1, -1):
                    if pa[y][xxx]:
                        pa[y][xxx], pa[y][xx] = pa[y][xx], pa[y][xxx]
                        break
    return pa


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
Q = deque([[copy(board), 0]])
while Q:
    now_board, now_cnt = Q.popleft()
    if now_cnt != 5:
        copied = copy(now_board)
        t = to_left(copied)
        print()
        for i in t:
            print(i)
        Q.append([t, now_cnt + 1])
