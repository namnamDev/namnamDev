from collections import deque

N, M = map(int, input().split())
tree = [[] for _ in range(N + 1)]
for m in range(M):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)
an = 0
minCnt = N ** N
for i in range(1, N + 1):
    vi = [0] * (N + 1)
    vi[i] = 1
    q = deque([i])
    while q:
        n = q.popleft()
        nowLine = tree[n]
        for f in nowLine:
            if not vi[f]:
                vi[f] = vi[n] + 1
                q.append(f)
    a = sum(vi) - N
    if minCnt > a:
        minCnt = a
        an = i
print(an)