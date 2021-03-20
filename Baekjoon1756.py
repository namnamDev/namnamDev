import sys

sys.stdin = open("Baekjoon1756.txt")

D, N = map(int, input().split())
arr, end = list(map(int, input().split())) + [0], list(map(int, input().split()))
visited = [0] * (D + 1)
temp = 0
maxs = [0, 0]
for i in end:
    if i < maxs[0] and arr[maxs[1] - 1] <= i:
        maxs[1] -= 1
        visited[maxs[1]] = 1
    else:
        for g in range(D):
            if visited[g] == 0:
                if i > arr[g]:
                    maxs = [i, g]
                    visited[g] = 1
                    break
            else:
                visited[g - 1] = 1

print(visited.index(1))
