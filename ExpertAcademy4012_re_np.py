import sys

sys.stdin = open("ExpertAcademy4012.txt")


def food_value(arr):
    res = 0
    for i in range(len(arr) - 1):
        for g in range(i + 1, len(arr)):
            res += board[arr[i]][arr[g]] + board[arr[g]][arr[i]]
    return res


def powerset(cnt, val, arr, idx):
    if cnt == N // 2:
        global min_cnt
        t1 = ''
        t2 = ''
        for i in arr:
            t1 += str(i)
        for i in range(N):
            if not vi[i]:
                t2 += str(i)
        if food.get(t1, True):
            food[t1] = food_value(arr)
        if food.get(t2):
            min_val = min(min_val, abs(food[t1] - food[t2]))

        return
    for g in range(idx + 1, N):
        if not vi[g]:
            vi[g] = 1
            powerset(cnt + 1, val + board[idx][g] + board[g][idx], arr + [g], g)
            vi[g] = 0


for tc in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    min_cnt = 99999999999999999999
    food = {}
    for i in range(N):
        vi = [0] * N
        vi[i] = 1
        powerset(1, 0, [i], i)
    print("#{} {}".format(tc + 1, min_cnt))
