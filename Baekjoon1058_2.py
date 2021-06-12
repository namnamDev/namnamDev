import sys

sys.stdin = open('Baekjoon1058.txt')


def dfs(idx, arr):
    vi[idx] = 1
    temp = board[idx]
    for i in range(N):
        if temp[i] == 'Y' and not vi[i]:
            global cnt
            cnt += 1
            dfs(i, arr + [i])


N = int(input())
board = [list(input()) for _ in range(N)]
vi = [0] * N
max_cnt = 0
for i in range(N):
    cnt = 0
    if not vi[i]:
        dfs(i, [])
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
