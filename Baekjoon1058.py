import sys

sys.stdin = open('Baekjoon1058.txt')


def dfs(idx, nums):
    print(nums)
    if vi[idx]:
        global maxcnt
        maxcnt = max(maxcnt, nums)
        return
    vi[idx] = 1
    temp = board[idx]
    for i in range(N):
        if temp[i] == 'Y' and i != s:
            dfs(i, nums + 1)


N = int(input())
board = [list(input()) for _ in range(N)]
vi = [0] * N
maxcnt = 0
for s in range(N):
    dfs(s, 0)
print(maxcnt)
