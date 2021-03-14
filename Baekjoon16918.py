import sys
from collections import deque

sys.stdin = open("Baekjoon16918.txt")

diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]
R, C, N = map(int, input().split())
arr = [list(input()) for _ in range(R)]
Q = deque()
for i in range(R):
    for g in range(C):
        if arr[i][g] == '.':
            arr[i][g] = 0
        else:
            arr[i][g] = 2

cnt = 0
while cnt < N - 1:
    temp = deque()
    for i in range(R):
        for g in range(C):
            if arr[i][g] == 0:
                arr[i][g] = 3
            elif arr[i][g] != 1:
                arr[i][g] -= 1
            else:
                arr[i][g] = 0
                temp.append([i, g])

    while len(temp) != 0:
        now = temp.popleft()
        for i in range(4):
            wy = now[0] + diry[i]
            wx = now[1] + dirx[i]
            if 0 <= wy < R and 0 <= wx < C:
                arr[wy][wx] = 0
    cnt += 1

an = [""] * R
for i in range(R):
    for g in range(C):
        if arr[i][g]:
            an[i] += "O"
        else:
            an[i] += "."

for i in an:
    print(i)
print()
