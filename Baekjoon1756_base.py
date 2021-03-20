import sys

sys.stdin = open("Baekjoon1756.txt")

D, N = map(int, input().split())
arr, end = list(map(int, input().split())) + [0], list(map(int, input().split()))
visited = [0] * (D + 1)
for i in end:
    for g in range(D):
        if visited[g] == 0:
            if i > arr[g]:
                visited[g] = 1
                break
        else:
            visited[g - 1] = 1

print(visited.index(1))
