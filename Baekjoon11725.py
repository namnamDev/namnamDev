import sys

sys.stdin = open('Baekjoon11725.txt')


def tree(idx):
    v[idx] = 1
    line = board[idx]
    for i in range(N + 1):
        if line[i] and not v[i]:
            v[i] = 1
            treeM[i] = idx
            tree(i)


N = int(input())
board = [[0] * (N + 1) for _ in range(N + 1)]
v = [0] * (N + 1)
treeM = [0] * (N + 1)
for i in range(N - 1):
    m, s = map(int, input().split())
    board[m][s] = 1
    board[s][m] = 1

tree(1)
for i in range(2, N + 1):
    print(treeM[i])
# tree = [[] for _ in range(N + 1)]
# # treeM = [0] * (N + 1)
# # print(N)
# for i in range(N - 1):
#     m, s = map(int, input().split())
#     # print(m, s)
#     tree[m] += [s]
#     tree[s] += [m]
#     # treeM[m] = s
# for i in tree:
#     print(i)
# # for i in range(1, N):
# #     print(treeM[i])
