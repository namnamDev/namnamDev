import sys

sys.stdin = open('Baekjoon1922.txt')

from collections import deque

N = int(input())
M = int(input())
board = [[0] * N for _ in range(N)]
tree = [[] for _ in range(N + 1)]
for i in range(M):
    x, y, pay = map(int, input().split())
    y -= 1
    x -= 1
    tree[x].append([y, pay])
    tree[y].append([x, pay])

vi = [9999999999] * N
vi[0] = 0
Q = deque([0])
while Q:
    now = Q.popleft()
    tempArr = tree[now]
    nowPay = vi[now]
    print(now, tempArr)
    for i in tempArr:
        if nowPay + i[1] < vi[i[0]]:
            vi[i[0]] = nowPay + i[1]
            Q.append(i[0])
    print(vi)
print(sum(vi), vi)
