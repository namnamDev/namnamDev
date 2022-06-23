from collections import deque

N = int(input())
M = int(input())
tree = [[] for _ in range(N)]
vi = [3] * N
vi[0] = 0
for _ in range(M):
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    tree[s].append(e)
    tree[e].append(s)
Q = deque([0])
while Q:
    n = Q.popleft()
    for one in tree[n]:
        if vi[n] + 1 < vi[one]:
            vi[one] = vi[n] + 1
            Q.append(one)
tot = 0
for one in vi:
    if one < 3:
        tot += 1
print(tot - 1)