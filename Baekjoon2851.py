import sys

sys.stdin = open("Baekjoon2851.txt")


def choose(sums, depth, idx):
    global minCha
    if depth == 10:
        minCha = min(sums, minCha)
        return
    if minCha < abs(100 - sums):
        return
    for i in range(idx, N):
        choose(sums + arr[i], depth + 1, idx + 1)


N = 10
arr = [int(input()) for _ in range(N)]
print(arr)
minCha = 100
for g in range(N):
    choose(0, 0, g)
