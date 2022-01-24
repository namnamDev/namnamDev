import sys

sys.stdin = open("Baekjoon9934.txt")


def treeIn(depth, n, idx):
    print(idx)
    if depth == l - 1:
        tree[idx] = n
        print(tree)
        return
    if not tree[idx * 2 + 1]:
        print(tree)
        treeIn(depth + 1, n, idx * 2 + 1)
    elif not tree[idx]:
        tree[idx] = n
        print(tree)
    else:
        print(tree)
        treeIn(depth + 1, n, idx * 2 + 2)


l = int(input())
arr = list(map(int, input().split()))
tree = [0] * (2 ** l - 1)
print(tree)
print(arr)
for i in range(len(arr)):
    print(arr[i])
    treeIn(0, arr[i], 0)
print(tree)
# 0        0
# 1      1     2
# 2  3   4    5    6
# 3 7  8 9 10 11 12  13 14
# 2^4
