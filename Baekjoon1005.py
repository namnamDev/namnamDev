import sys

sys.stdin = open("Baekjoon1005.txt")


def trees(idx):
    if vi[idx]:
        return
    lines = tree[idx]
    if not len(lines):
        vi[idx] = times[idx]
        return
    mt = []
    for ones in range(len(lines)):
        o = lines[ones]
        trees(o)
        mt.append(vi[o])
    vi[idx] = max(mt) + times[idx]


for tc in range(int(input())):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    tree = [[] for _ in range(N + 1)]
    for i in range(K):
        pre, aft = map(int, input().split())
        tree[aft].append(pre)
    W = int(input())
    vi = [0] * (N + 1)
    trees(W)
    print(vi[W])
