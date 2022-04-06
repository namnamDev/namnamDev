from collections import deque

N, K = map(int, input().split())
vi = [100001] * 100001
vi[N] = 1
dr = [-1, 1]
Q = deque([N])
while Q:
    n = Q.popleft()
    for d in range(2):
        wy = n + dr[d]
        if 0 <= wy < 100001 and vi[n] + 1 < vi[wy]:
            vi[wy] = vi[n] + 1
            Q.append(wy)
    if 0 < 2 * n < 100001 and vi[n] <= vi[2 * n]:
        vi[2 * n] = vi[n]
        Q.append(2 * n)
print(vi[K] - 1)