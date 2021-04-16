import sys

sys.stdin = open('ExpertAcademy11763.txt')


def myfunction(num, arr, val):
    if num == N - 1:
        global res
        val += board[arr[-1]][0]
        res = min(val, res)
        return
    else:
        for i in range(1, N):
            if not visited[i]:
                visited[i] = 1
                myfunction(num + 1, arr + [i], val + board[arr[-1]][i])
                visited[i] = 0


for tc in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    temp = list(range(N))
    visited = [0] * N
    visited[0] = 1
    res = 100 * N * N
    myfunction(0, [0], 0)
    print("#{} {}".format(tc + 1, res))
