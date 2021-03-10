import sys

sys.stdin = open("Baekjoon16457.txt")


def dfs(cnt):
    if cnt == n:
        global an
        fin = 0
        for i in range(m):
            temp = 0
            for g in range(k):
                if visited[arr[i][g]]:
                    temp += 1
            if temp == k:
                fin += 1

        if an < fin:
            an = fin
        return
    else:
        for i in range(1, len(visited)):
            if visited[i] == 0:
                visited[i] = 1
                dfs(cnt + 1)
                visited[i] = 0
                # dfs(cnt + 1)


n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
visited = [0] * (2 * n + 1)
print(n, m, k)
an = 0
dfs(0)
print(an)
