import sys

sys.stdin = open("Baekjoon11437.txt")

# def fin_pa(idx):
#     if not tree[idx][0]:
#         return 1
#     else:
from collections import deque

N = int(input())
tree = [[] for _ in range(N + 1)]
for n in range(N - 1):
    p, s = map(int, input().split())
    # print(s, p)
    tree[s].append(p)
    tree[p].append(s)
    # print(tree)
M = int(input())
for m in range(M):
    a, b = map(int, input().split())
    vi = [0] * (N + 1)
    # vi[a] = -1
    # vi[b] = -2
    Q = deque([a, b])
    an = 0
    while Q:
        now = Q.popleft()
        # print(now, tree[now])
        if vi[now]:
            an = now
            if now == a:
                an = tree[a]
            elif now == b:
                an = tree[b]
            # print("point", an)
            break
        vi[now] = 1
        # p = tree[now][0]
        now_line = tree[now]
        for pa in now_line:
            # if not vi[pa]:
            Q.append(pa)

    # print(vi)/
    print("an", an)
#   1
#  2 3
# 4    7
