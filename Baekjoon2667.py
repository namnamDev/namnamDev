import sys

sys.stdin = open('Baekjoon2667.txt')
from collections import deque

N = int(input())
board = [list(map(int, input())) for _ in range(N)]
answers = []
diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]
vi = [[0] * N for _ in range(N)]
for yy in range(N):
    for xx in range(N):
        if board[yy][xx] and not vi[yy][xx]:
            cnt = 1
            Q = deque([[yy, xx]])
            vi[yy][xx] = 1
            while Q:
                now = Q.popleft()
                for d in range(4):
                    wy = diry[d] + now[0]
                    wx = dirx[d] + now[1]
                    if 0 <= wy < N and 0 <= wx < N and board[wy][wx] and not vi[wy][wx]:
                        vi[wy][wx] = 1
                        cnt += 1
                        Q.append([wy, wx])
            answers.append(cnt)
print(len(answers))
answers.sort()
for i in answers:
    print(i)
