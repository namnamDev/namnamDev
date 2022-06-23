from collections import deque

N, M, K, X = map(int, input().split())
tree = [[] for _ in range(N + 1)]
visit = [N + 1] * (N + 1)
visit[0] = 0
for _ in range(M):
    s, e = map(int, input().split())
    tree[s].append(e)
visit[X] = 0
Q = deque([X])
while Q:
    n = Q.popleft()
    for one in tree[n]:
        if visit[n] + 1 < visit[one]:
            visit[one] = visit[n] + 1
            Q.append(one)
res = []
for idx in range(1, N + 1):
    if visit[idx] == K:
        res.append(idx)
if not res:
    res = [-1]

for one in res:
    print(one)
