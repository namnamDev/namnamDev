import sys

sys.stdin = open('Baekjoon16940.txt')
from collections import deque

N = int(input())
tree = [[] for _ in range(N + 1)]

vi = [0] * (N + 1)
for i in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

order = list(map(int, input().split()))
Q = deque([order[0]])
vi[order[0]] = 1
order[order.index(vi[order[0]])] = -1
maxIdx = 0
answer = 1
while Q:
    now = Q.popleft()
    nowline = tree[now]
    tempMax = 0
    for i in range(len(nowline)):
        if not vi[nowline[i]]:
            vi[nowline[i]] = vi[now] + 1
            Q.append(nowline[i])
            temp = order.index(nowline[i])
            order[temp] = -1
            tempMax = max(tempMax, temp)
    # print(order, tempMax)
    if tempMax:
        for i in range(maxIdx, tempMax + 1):
            if order[i] != -1:
                answer = 0
                Q = []
                break
    maxIdx = max(maxIdx, tempMax)
print(answer)
