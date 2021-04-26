import sys

sys.stdin = open("Baekjoon4386.txt")


def dik(num):
    start = num
    board = [INF] * N
    board[start] = 0
    min_road = INF
    min_idx = 0
    vi = [0] * N
    vi[num] = 1
    Q = [[num, 0]]
    while len(Q):
        now = Q.pop(0)
        vi[now[1] - 1] = 1
        print(now, 'ssdsd')
        for i in range(N):
            if not vi[i]:
                calc = ((arr[now[1]][0] - arr[i][0]) ** 2 + (arr[now[1]][1] - arr[i][1]) ** 2) ** 0.5
                print(calc)
                Q.append([calc, i])
        print(Q)
        Q.sort()
        if now[0] < board[now[1]]:
            board[now[1]] = now[0]
            Q.append(arr[now[1]])
    print(board)


INF = 999999999
N = int(input())
arr = [list(map(float, input().split())) for _ in range(N)]
print(arr)
dik(0)
