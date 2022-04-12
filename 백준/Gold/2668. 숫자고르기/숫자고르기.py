from collections import deque

N = int(input())
deg = [0] * (N + 1)
tree = [0] * N
for s in range(N):
    e = int(input())
    deg[e] += 1
    tree[s] = e
Q = deque([])
for i in range(1, N + 1):
    if not deg[i]:
        Q.append(i)
if len(Q):
    while Q:
        n = Q.popleft()
        e = tree[n - 1]
        deg[e] -= 1
        if not deg[e]:
            Q.append(e)
    an = []
    for i in range(1, N + 1):
        if deg[i]:
            an.append(i)
    print(len(an))
    for i in an:
        print(i)
else:
    print(N)
    for i in range(1, N + 1):
        print(i)
