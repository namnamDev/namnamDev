import sys
from pprint import pprint

sys.stdin = open("Baekjoon2224.txt")


def dfs(now, temp):
    global visited
    global board
    global cnt
    visited[now] = 1
    if 1 not in board[now]:
        # board[now] = [0]
        print(temp)
        return
    else:
        for i in range(SIZE):
            if board[now][i] and visited[i] != 1:
                # print(now, i)
                temp[now][1].append(i)
                cnt += 1
                dfs(i, temp)


SIZE = 57  # 마지막에 +65 필수
T = int(input())
arr = [0] * T
for i in range(T):
    arr[i] = list(input().split())
# print(arr, ord("A"), ord("Z"), ord("a"), ord("z"))
# print(arr, ord("A") - 65, ord("Z") - 65, ord("a") - 65, ord("z") - 65)
board = [[0] * SIZE for _ in range(SIZE)]
first = []
for g in range(T):
    board[ord(arr[g][0]) - 65][ord(arr[g][2]) - 65] = 1

visited = [0] * SIZE
temp = [i] * SIZE
for i in range(SIZE):
    temp[i] = [i, []]
cnt = 0
for re in range(SIZE):
    dfs(re, temp)
# for i in range(SIZE):
