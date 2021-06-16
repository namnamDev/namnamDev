import sys

sys.stdin = open('Baekjoon11725.txt')

N = int(input())
trees = [[] for _ in range(N + 1)]
v = [0] * (N + 1)
treeM = [0] * (N + 1)
for i in range(N - 1):
    m, s = map(int, input().split())
    trees[m].append(s)
    trees[s].append(m)

stacks = [1]
while stacks:
    now = stacks.pop()
    v[now] = 1
    for i in trees[now]:
        if not v[i]:
            if not treeM[i]:
                treeM[i] = now
            stacks.append(i)
for i in range(2, N + 1):
    print(treeM[i])
