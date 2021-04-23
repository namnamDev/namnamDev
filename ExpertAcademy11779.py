import sys

sys.stdin = open('ExpertAcademy11779.txt')


def my_function(cnt, val, arr):
    global min_cnt
    # print(cnt, val)
    if 1000000 <= val or val <= 0:
        return
    if cnt > min_cnt:
        return
    if val == M:
        print(cnt, val, arr)
        min_cnt = min(val, cnt)
        return
    if val < M:
        my_function(cnt + 1, val * 2, arr + [val * 2])
        my_function(cnt + 1, val + 1, arr + [val + 1])
    else:
        temp = val - M
        if temp > 10:
            return
        my_function(cnt + 1, val - 10, arr + [val - 10])
        my_function(cnt + 1, val - 1, arr + [val - 1])
    # if 10 < val - M:
    #     my_function(cnt + 1, val - 10, arr + [val - 10])
    # else:
    #     my_function(cnt + 1, val - 1, arr + [val - 1])
    # if 1 < M - val:
    #     my_function(cnt + 1, val * 2, arr + [val * 2])
    # else:
    #     my_function(cnt + 1, val + 1, arr + [val + 1])


'3 6 12 13 14 15'
for tc in range(int(input())):
    N, M = map(int, input().split())
    min_cnt = M - N
    my_function(0, N, [N])
    print("#{} {}".format(tc + 1, min_cnt))
