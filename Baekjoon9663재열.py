import sys


def queen(N, depth):
    temp = 0
    print(N, depth)
    for i in visited:
        print(i)
    if depth == N - 1:
        # for i in visited:
        #     print(i)
        for i in range(N):
            if visited[N - 1][i] == 0:
                print('true')
                global cnt
                cnt += 1
        return

    for l in range(N):
        if visited[depth][l] > 0:
            temp += 1
    if temp == N:
        return
    for j in range(N):
        if visited[depth][j] == 0:
            visited[depth][j] += 1
            for k in range(1, N - depth):
                visited[depth + k][j] += 1
                if j + k < N:
                    visited[depth + k][j + k] += 1
                if j - k >= 0:
                    visited[depth + k][j - k] += 1

            queen(N, depth + 1)
            visited[depth][j] -= 1
            for k in range(1, N - depth):
                visited[depth + k][j] -= 1
                if j + k < N:
                    visited[depth + k][j + k] -= 1
                if j - k >= 0:
                    visited[depth + k][j - k] -= 1


num = int(input())
cnt = 0
used = []
visited = [[0] * num for _ in range(num)]
queen(num, 0)
print(cnt)
# dfs(0, 0, board, 0)
# print(len(used), cnt)
