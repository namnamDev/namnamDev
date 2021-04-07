import sys
from collections import deque

sys.stdin = open('Baekjoon15686.txt')
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]
print(board)
Q = deque()
for i in range(N):
    for g in range(N):
        if board[i][g] == 1:
            Q.append([i, g])
print(Q)
resultarr = []
while len(Q):
    tempQ = deque()
    tempQ.append(Q.popleft())
    print(tempQ)
    visited = [[0] * N for _ in range(N)]
    visited[tempQ[0][0]][tempQ[0][1]] = 1
    cont = True
    while len(tempQ) and cont:
        tempQQ = tempQ.popleft()
        for i in visited:
            print(i)
        print()
        for dirs in range(4):
            wy = diry[dirs] + tempQQ[0]
            wx = dirx[dirs] + tempQQ[1]
            if 0 <= wy < N and 0 <= wx < N and visited[wy][wx] == 0:
                visited[wy][wx] = 1 + visited[tempQQ[0]][tempQQ[1]]
                if board[wy][wx] == 2:
                    resultarr += [visited[tempQQ[0]][tempQQ[1]]]
                    cont = False
                    break
                tempQ.append([wy, wx])

    for i in visited:
        print(i)
print(resultarr)
print(sum(resultarr))
