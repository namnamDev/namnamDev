import sys

sys.stdin = open('Baekjoon17352.txt')
N = int(input())
tree = [[] for _ in range(N)]
for i in range(N - 2):
    x, y = map(int, input().split())
    y -= 1
    x -= 1
    tree[x].append(y)
    tree[y].append(x)

vi = [0] * N
Q = [0]
vi[0] = 1
road = []

while Q:
    now = tree[Q.pop()]
    for i in now:
        if not vi[i]:
            vi[i] = 1
            Q.append(i)
            road.append(i)
an = 0
for ii in range(N):
    if not vi[ii]:
        an = ii
        break
print(str(1) + " " + str(an + 1))
