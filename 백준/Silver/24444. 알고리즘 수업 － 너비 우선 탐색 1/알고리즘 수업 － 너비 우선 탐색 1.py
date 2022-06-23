from collections import deque

N, M, R = map(int, input().split())
tree = [[] for _ in range(N + 1)]
vi = [0] * (N + 1)
for _ in range(M):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)
for i in tree:
    i.sort()
Q = deque([R])
cnt = 1
vi[R] = cnt
while Q:
    n = Q.popleft()
    nowLine = tree[n]
    for i in nowLine:
        if not vi[i]:
            cnt += 1
            vi[i] = cnt
            Q.append(i)
for i in range(1, N + 1):
    print(vi[i])