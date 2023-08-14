import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
tree = [[] for _ in range(N + 1)]
visit = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

cnt = 0
for idx in range(1, N + 1):
    if not visit[idx]:
        cnt += 1
        Q = deque([idx])
        while Q:
            now = Q.popleft()
            now_line = tree[now]
            for w in now_line:
                if not visit[w]:
                    visit[w] = cnt
                    Q.append(w)

tree_list = list(set(visit))
tree_cnt = len(tree_list) - 2
not_connected_cnt = visit.count(0) - 1
need_line = not_connected_cnt + tree_cnt
answer = need_line
if M + need_line > N - 1:
    answer += M + need_line - (N - 1)
print(answer)
