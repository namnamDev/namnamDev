from collections import deque

N, K = map(int, input().split())
vi = [100001] * 100001
vi[N] = 1
Q = deque([N])
dr = [-1, 1]
min_K = 100001
min_cnt = 0
while Q:
    n = Q.popleft()
    if vi[n] <= vi[K]:
        if n == K:
            if vi[n] < min_K:
                min_cnt = 1
                min_K = vi[n]
            elif vi[n] == min_K:
                min_cnt += 1
        for d in dr:
            w = n + d
            if 0 <= w < 100001:
                if vi[w] >= vi[n] + 1:
                    vi[w] = vi[n] + 1
                    Q.append(w)
        if 0 < n:
            w = n * 2
            if w < 100001:
                if vi[w] >= vi[n] + 1:
                    vi[w] = vi[n] + 1
                    Q.append(w)
print(vi[K] - 1)
print(min_cnt)
