import sys

sys.stdin = open("ExpertAcademy4012.txt")


def food_value(t1_arr):
    food_val = 0
    for i in range(len(t1_arr) - 1):
        for g in range(i + 1, len(t1_arr)):
            food_val += board[t1_arr[i]][t1_arr[g]] + board[t1_arr[g]][t1_arr[i]]

    # print(t1_arr, food_val)
    return food_val


def powerset(cnt, val, arr, idx):
    if cnt == N // 2:
        global min_val
        t1 = ''
        t2 = ''
        # arr2 = []
        for i in arr:
            t1 += str(i)
        for i in range(N):
            if not vi[i]:
                t2 += str(i)
        if food.get(t1, True):
            food[t1] = food_value(arr)
            # print(t1, food[t1], 'in')
        # print(t2, food.get(t2), 'two')
        if food.get(t2):
            # print(t1, t2, abs(food[t1] - food[t2]))
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
    min_val = 99999999999999999999
    food = {}
    for i in range(N):
        vi = [0] * N
        vi[i] = 1
        powerset(1, 0, [i], i)
    print("#{} {}".format(tc + 1, min_val))
