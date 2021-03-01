import sys

sys.stdin = open("ExpertAcademy2805.txt")


def cal(li):
    sums = 0
    f = 0
    for g in range(mid):
        temp = li[g][mid - f:mid + f + 1]
        # print(temp, mid - f, mid + f + 1)
        sums += sum(temp)
        f += 1
    return sums


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [0] * N
    for i in range(N):
        board[i] = list(map(int, input()))
    mid = N // 2
    rev = [0] * mid
    for i in range(mid):
        rev[i] = board[N - i - 1]
    # print(rev)
    an = cal(board) + cal(rev) + sum(board[mid])
    print("#{} {}".format(tc, an))
