import sys

sys.stdin = open('Baekjoon5971.txt')


def findPa(son):
    global an
    if not tree[son][1] or an:
        return
    else:
        if tree[son][1] not in a1:
            a1.append(tree[son][1])
            findPa(tree[son][1])
        else:
            an = tree[son][1]


N, M = map(int, input().split())
tree = [[0, 0] for _ in range(N + 1)]
tree[1] = [1, 0]
for i in range(2, N + 1):
    tree[i] = [i, int(input())]

where = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    a1 = [where[i][0], where[i][1]]
    an = 0
    if where[i][0] == where[i][1]:
        an = where[i][0]
    findPa(where[i][0])
    # print(where[i], a1)
    findPa(where[i][1])
    # print(where[i], a1)
    print(an)
# print(tree)
# print(where)
