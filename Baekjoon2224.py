import sys

sys.stdin = open("Baekjoon2224.txt")
SIZE = 57  # 마지막에 +65 필수
T = int(input())
arr = [0] * T
for i in range(T):
    arr[i] = list(input().split())
print(arr, ord("A"), ord("Z"), ord("a"), ord("z"))
print(arr, ord("A") - 65, ord("Z") - 65, ord("a") - 65, ord("z") - 65)
board = [[0] * SIZE for _ in range(SIZE)]
first = -1
for g in range(T):
    board[ord(arr[g][0]) - 65][ord(arr[g][2]) - 65] = 1
print(board)

for i in range(SIZE):
    for g in range(SIZE):
        if board[i][g]:
            first = i
            break
    if first != -1:
        break

visited = [0] * SIZE
visited[first] = 1
Q = [first]
while len(Q) != 0:
    now = Q.pop()
    print(now, end=" ")
    for i in range(SIZE):
        if board[now][i] and visited[i] != 1:
            visited[i] = 1
            Q.append(i)
            print(i)
