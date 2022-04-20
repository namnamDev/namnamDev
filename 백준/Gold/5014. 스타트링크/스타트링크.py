from collections import deque

F, S, G, U, D = map(int, input().split())
vi = [0] * (F + 1)
vi[S] = 1
Q = deque([S])
while Q:
    n = Q.popleft()
    if vi[G]:
        break
    u = n + U
    d = n - D
    if u <= F and not vi[u]:
        vi[u] = vi[n] + 1
        Q.append(u)
    if 0 < d and not vi[d]:
        vi[d] = vi[n] + 1
        Q.append(d)
if vi[G]:
    print(vi[G] - 1)
else:
    print("use the stairs")