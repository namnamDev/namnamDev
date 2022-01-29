import sys

sys.stdin = open("Baekjoon1240.txt")


def dfs(idx):
    if idx == end:
        return
    nowList = tree[idx]
    for now in nowList:
        if not vi[now[0]]:
            vi[now[0]] = vi[idx] + now[1]
            dfs(now[0])


N, W = map(int, input().split())
tree = [[] for _ in range(N + 1)]
for node in range(N - 1):
    y, x, c = map(int, input().split())
    tree[y].append([x, c])
    tree[x].append([y, c])
wList = []
for w in range(W):
    wList.append(list(map(int, input().split())))
for wl in wList:
    vi = [0] * (N + 1)
    start = wl[0]
    end = wl[1]
    vi[start] = 1
    dfs(start)
    print(vi[end] - 1)
