import sys

def bfs(pidx):
    vi = [0] * (V + 1)
    vi[pidx] = 1
    stack = [pidx]
    while stack:
        now = stack.pop()
        now_line = tree[now]
        for e, v in now_line:
            if not vi[e]:
                vi[e] = vi[now] + v
                stack.append(e)
    return vi


V = int(sys.stdin.readline())
tree = [[] for _ in range(V + 1)]
for _ in range(V):
    t = list(map(int, sys.stdin.readline().split()))
    s = t[0]
    for es in range(1, len(t) - 1, 2):
        e, v = t[es], t[es + 1]
        tree[s].append([e, v])
        tree[e].append([s, v])
max_cnt = 0
pVi = bfs(1)
ppVi = bfs(pVi.index(max(pVi)))
print(max(ppVi) - 1)