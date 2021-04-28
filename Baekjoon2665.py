import sys

sys.stdin = open('Baekjoon2665.txt')

from collections import deque

N = int(input())
board = [list(map(int, input())) for _ in range(N)]
br = [[N * N] * N for _ in range(N)]
dry = [-1, 1, 0, 0]
drx = [0, 0, -1, 1]
start = [0, 0]
end = [N - 1, N - 1]
Q = deque([start])
br[0][0] = 0
while len(Q):
    now = Q.popleft()
    for i in range(4):
        wy = now[0] + dry[i]
        wx = now[1] + drx[i]
        if 0 <= wy < N and 0 <= wx < N:
            if not board[wy][wx]:
                if br[now[0]][now[1]] + 1 < br[wy][wx]:
                    br[wy][wx] = br[now[0]][now[1]] + 1
                    Q.append([wy, wx])
            else:
                if br[now[0]][now[1]] < br[wy][wx]:
                    br[wy][wx] = br[now[0]][now[1]]
                    Q.append([wy, wx])
print(br[N - 1][N - 1])
