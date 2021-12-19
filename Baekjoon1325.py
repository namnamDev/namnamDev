import sys

sys.stdin = open('Baekjoon1326.txt')

from collections import deque

N = int(input())
bridge = list(map(int, input().split()))
start, end = map(int, input().split())
vi = [-1] * N
start -= 1
end -= 1
vi[start] = 0
Q = deque([start])
while Q:
    now = Q.popleft()
    num = bridge[now]
    rc = lc = 1

    while now + rc * num < N:
        if vi[now + rc * num] < 0:
            vi[now + rc * num] = vi[now] + 1
            Q.append(now + rc * num)
        rc += 1

    while 0 <= now - lc * num:
        if vi[now - lc * num] < 0:
            vi[now - lc * num] = vi[now] + 1
            Q.append(now - lc * num)
        lc += 1
    if vi[end] > 0:
        break
print(vi[end])
