import sys

sys.stdin = open('ExpertAcademy1232.txt')


def my_order(num):
    # print(arr[num])
    t = arr[num][2]
    if t != '/' and t != '-' and t != '+' and t != '*':
        # print(arr[num][1])
        return arr[num][1]
    else:
        # print(t, 'here')
        if t == '/':
            arr[num][2] = my_order(arr[num][0]) // my_order(arr[num][1])
        elif t == '*':
            arr[num][2] = my_order(arr[num][0]) * my_order(arr[num][1])
        elif t == '+':
            arr[num][2] = my_order(arr[num][0]) + my_order(arr[num][1])
        else:
            arr[num][2] = my_order(arr[num][0]) - my_order(arr[num][1])
        # print(arr[num][2], '-' * 10)
        return arr[num][2]


for tc in range(10):
    N = int(input())
    arr = [[0] * 3 for _ in range(N + 1)]
    for i in range(N):
        line = list(input().split())
        if len(line) > 2:
            arr[int(line[0])][2] = line[1]
            arr[int(line[0])][0] = int(line[2])
            arr[int(line[0])][1] = int(line[3])
        else:
            arr[int(line[0])][1] = int(line[1])
    print("#{} {}".format(tc + 1, my_order(1)))
