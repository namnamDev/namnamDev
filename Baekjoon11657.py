import sys

sys.stdin = open("Baekjoon11657.txt")

from collections import deque

N, M = map(int, input().split())
tree = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, v = map(int, input().split())
    tree[s].append([e, v])
vi = [N * M * 10000] * (N + 1)
Q = deque([1])
cycle = [[] for _ in range(N + 1)]
answer = -1
vi[1] = vi[0] = 0

real_vi = [0] * (N + 1)


def dik(p_arr):
    while p_arr:
        now = p_arr.popleft()
        tree_line = tree[now]
        for e, v in tree_line:
            if v + vi[now] < vi[e]:
                vi[e] = v + vi[now]
                real_vi[e] += 1
                if v + vi[now] < 0:
                    return False
                p_arr.append(e)
    return True


if dik(Q):
    for i in range(2, N + 1):
        if real_vi[i]:
            print(vi[i])
        else:
            print(-1)
else:
    print(-1)

# while Q:
#     now = Q.popleft()
#     tree_line = tree[now]
#     for e, v in tree_line:
#         if v + vi[now] < vi[e]:
#             vi[e] = v + vi[now]
#             if e == 1 and v + vi[now] < 0:
#                 break
#             Q.append(e)
# for i in tree:
#     print(i)
